from collections import defaultdict
import hashlib
import threading
import time
import xml.etree.ElementTree as ET
from utils.logger import log

class Msg:
    def __init__(self, wxmsg):
        self.wxmsg = wxmsg
        self.hash = hashlib.md5(wxmsg.content.encode()).hexdigest()
        self.time = time.time()

class MsgRecords:
    def __init__(self,recent_time=60*60*3):
        self.msgs = defaultdict(list)
        self.recent_time = recent_time
        self.clean_thread = threading.Thread(target=self.clean)
        self.clean_thread.daemon = True
        self.clean_thread.start()

    def clean(self):
        while True:
            time.sleep(60)  # 每分钟清理一次
            for key in self.msgs:
                msgs = self.msgs[key]
                for msg in msgs:
                    if time.time() - msg.time > self.recent_time:
                        msgs.remove(msg)
                        log.info(f"remove_msg: {key}, {msg.hash}")

    def add_msg(self, wxmsg):
        if not wxmsg.from_group():
            return
        room_id = wxmsg.roomid
        msg = Msg(wxmsg)
        self.msgs[room_id].append(msg)
        log.info(f"add_msg:{msg.hash}")
    def get_recent_msg(self, room_id,wcf)->str:
        #整理为发言人:内容
        msgs = self.msgs[room_id]
        res = ""
        for item in msgs:
            if not item.wxmsg.is_text():
                continue
            name = wcf.get_alias_in_chatroom(item.wxmsg.sender,room_id)
            # 格式化时间
            formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item.time))
            res += f"{formatted_time} {name}:{item.wxmsg.content}\n"
        return res


def md5(text):
    return hashlib.md5(text.encode()).hexdigest()

if __name__ == "__main__":
    pass