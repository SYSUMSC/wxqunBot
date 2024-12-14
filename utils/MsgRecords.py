from collections import defaultdict
import hashlib
import threading
import time
import xml.etree.ElementTree as ET
from api.openaiApi import openaiApi
from utils.logger import log
from wcferry.client import Wcf
from config import tmp_dir
class Msg:
    def __init__(self, wxmsg):
        self.wxmsg = wxmsg
        self.img_info = ""
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
        if not wxmsg.is_text() and not wxmsg.type == 3:
            log.info(f"not text or img:{wxmsg.content}")
            return

        room_id = wxmsg.roomid
        msg = Msg(wxmsg)
        if wxmsg.type == 3:
            #时间戳+md5content生成保存路径
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
            msg.img_info = f"发送了图片，图片描述:{res}"
        self.msgs[room_id].append(msg)
        log.info(f"add_msg:{msg.hash}")
    def get_recent_msg(self, room_id,wcf)->str:
        #整理为发言人:内容
        msgs = self.msgs[room_id]
        res = ""
        for item in msgs:
            if not item.wxmsg.is_text() and not item.wxmsg.type == 3:
                continue
            name = wcf.get_alias_in_chatroom(item.wxmsg.sender,room_id)
            # 格式化时间
            formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item.time))
            if item.wxmsg.type == 3:
                res += f"{formatted_time} {name}:{item.img_info}\n"
            else:
                res += f"{formatted_time} {name}:{item.wxmsg.content}\n"
        return res


def md5(text):
    return hashlib.md5(text.encode()).hexdigest()

if __name__ == "__main__":
    pass