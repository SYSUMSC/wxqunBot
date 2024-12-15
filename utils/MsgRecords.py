from collections import defaultdict
import hashlib
import threading
import time
import xml.etree.ElementTree as ET
from api.openaiApi import openaiApi
from utils.img import convert_gif_to_jpg, get_img_ext
from utils.logger import log
from wcferry.client import Wcf
from config import tmp_dir
from utils.download import download_file
from utils.xml import parse_xml
import os
class Msg:
    def __init__(self, wxmsg):
        self.wxmsg = wxmsg
        self.content = ""
        self.hash = hashlib.md5(wxmsg.content.encode()).hexdigest()
        self.time = time.time()


class MsgRecords:
    def __init__(self,recent_time=60*60*3):
        self.msgs = defaultdict(list)
        self.recent_time = recent_time
        self.clean_thread = threading.Thread(target=self.clean)
        self.clean_thread.daemon = True
        self.clean_thread.start()
        self.oai = openaiApi()

    def clean(self):
        while True:
            time.sleep(60)  # 每分钟清理一次
            for key in self.msgs:
                msgs = self.msgs[key]
                for msg in msgs:
                    if time.time() - msg.time > self.recent_time:
                        msgs.remove(msg)
                        log.info(f"remove_msg: {key}, {msg.hash}")

    def add_msg(self, wxmsg,wcf:Wcf):
        # if not wxmsg.from_group():
        #     return
        #只接收text或者img
        if not wxmsg.is_text() and not wxmsg.type == 3 and not wxmsg.type == 47:
            log.info(f"not text or img:{wxmsg.content}")
            return

        room_id = wxmsg.roomid
        msg = Msg(wxmsg)
        if wxmsg.type == 3:
            log.info(f"尝试下载 {tmp_dir}")
            img_path = wcf.download_image(wxmsg.id, wxmsg.extra, tmp_dir,300)
            if not img_path:
                log.error(f"download image failed:{wxmsg.id}")
                return
            log.info(f"download image success:{wxmsg.id}")
            #发给llm
            prompt = "中文描述图片"
            res,errmsg = self.oai.chat_img(prompt,img_path)
            if not res:
                log.error(f"chat_img failed:{errmsg}")
                return
            msg.content = f"发送了图片，描述:{res}"
        elif wxmsg.type == 47:
            root = parse_xml(wxmsg.content)
            url = root.find("emoji").get("cdnurl")
            log.info(f"尝试下载 {url}")
            img_path = f"{tmp_dir}/{wxmsg.id}"
            download_file(url, img_path)
            if not img_path:
                log.error(f"download image failed:{url}")
                return
            log.info(f"download image success:{url}")
            # 根据二进制文件类型改后缀
            ext = get_img_ext(img_path)
            if ext == "gif":
                new_img_path = f"{img_path}.jpg"
                convert_gif_to_jpg(img_path, new_img_path)
                img_path = new_img_path
            else:
                new_img_path = f"{img_path}.{ext}"
                # 重命名文件
                os.rename(img_path,new_img_path)
            #发给llm
            prompt = "中文描述图片"
            res,errmsg = self.oai.chat_img(prompt,new_img_path)
            if not res:
                log.error(f"chat_img failed:{errmsg}")
                return
            msg.content = f"发送了图片，描述:{res}"
        else:
            msg.content = wxmsg.content
        self.msgs[room_id].append(msg)
        log.info(f"add_msg:{msg.hash} {msg.content} {msg.wxmsg.content}")
    def get_recent_msg(self, room_id,wcf)->str:
        #整理为发言人:内容
        msgs = self.msgs[room_id]
        max_msg = 20
        if len(msgs) > max_msg:
            msgs = msgs[-max_msg:]
        res = ""
        for item in msgs:
            if not item.content:
                continue
            name = wcf.get_alias_in_chatroom(item.wxmsg.sender,room_id)
            # 格式化时间
            formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item.time))
            res += f"{formatted_time} {name}:{item.content}\n"
        return res


def md5(text):
    return hashlib.md5(text.encode()).hexdigest()

if __name__ == "__main__":
    pass