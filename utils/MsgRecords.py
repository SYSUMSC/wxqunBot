from collections import defaultdict
import hashlib
import threading
import time
import xml.etree.ElementTree as ET

class Msg:
    def __init__(self, wxmsg):
        self.wxmsg = wxmsg
        self.hash = hashlib.md5(wxmsg.content.encode()).hexdigest()
        self.is_video = self.is_video(wxmsg)
        self.time = time.time()
        self.record_id = None
        self.record_id_condition = threading.Condition()  # 用于同步的条件变量

    @staticmethod
    def is_video(wxmsg) -> bool:
        if wxmsg.type == 49:
            try:
                root = ET.fromstring(wxmsg.content)
                finder_feed = root.find('appmsg/finderFeed')
                appname = root.find('appinfo/appname')
                if finder_feed is not None:
                    return True
                if appname is not None and (appname.text == "小红书" or appname.text == "哔哩哔哩"):
                    return True
                return False
            except Exception:
                return False
        if wxmsg.content.count("https://") > 1:
            return False
        if any(platform in wxmsg.content for platform in
                ["douyin.com", "抖音", "bilibili.com", "哔哩哔哩", "b23.tv", "xiaohongshu.com", "小红书"]):
            return True
        return False

class MsgRecords:
    def __init__(self):
        self.msgs = defaultdict(list)
        self.locks = defaultdict(threading.Lock)  # 每个(room_id, user_id)一个锁
        self.clean_thread = threading.Thread(target=self.clean)
        self.clean_thread.daemon = True
        self.clean_thread.start()

    def clean(self):
        while True:
            time.sleep(60)  # 每分钟清理一次
            for key in list(self.msgs.keys()):
                with self.locks[key]:
                    self.msgs[key] = [msg for msg in self.msgs[key] if time.time() - msg.time <= 600]
                    if not self.msgs[key]:
                        del self.msgs[key]

    def add_msg(self, wxmsg):
        if not wxmsg.from_group():
            return
        room_id = wxmsg.roomid
        user_id = wxmsg.sender
        key = (room_id, user_id)
        with self.locks[key]:
            msg = Msg(wxmsg)
            self.msgs[key].append(msg)
            print(f"Added msg: {room_id} {user_id} {msg.hash} is_video {msg.is_video}")

    def set_record_id(self, wxmsg, record_id):
        room_id = wxmsg.roomid
        user_id = wxmsg.sender
        key = (room_id, user_id)
        with self.locks[key]:
            msgs = self.msgs[key]
            for i, msg in enumerate(msgs):
                if msg.is_video and msg.hash == hashlib.md5(wxmsg.content.encode()).hexdigest():
                    msg.record_id = record_id
                    print(f"Setting record_id {record_id} for msg: {msg.hash}")
                    with msg.record_id_condition:
                        msg.record_id_condition.notify_all()
                    return

    def get_near_record_id(self, wxmsg):
        room_id = wxmsg.roomid
        user_id = wxmsg.sender
        key = (room_id, user_id)

        for _ in range(3):  # 尝试两次查找
            with self.locks[key]:
                msgs = self.msgs[key].copy()

            current_hash = hashlib.md5(wxmsg.content.encode()).hexdigest()
            current_index = None

            for i, msg in enumerate(msgs):
                if msg.hash == current_hash:
                    current_index = i
                    break
            if current_index is None:
                return None

            # 先向前面查找
            for i in range(current_index - 1, -1, -1):
                if msgs[i].is_video:
                    if msgs[i].record_id is not None:
                        return msgs[i].record_id
                    with msgs[i].record_id_condition:
                        print(f"Waiting for record_id to be set for msg: {msgs[i].hash}")
                        max_retry = 3
                        for retry in range(max_retry):
                            if msgs[i].record_id_condition.wait(timeout=10):
                                if msgs[i].record_id is not None:
                                    print(f"Retrieved record_id: {msgs[i].record_id} for msg: {msgs[i].hash}")
                                    return msgs[i].record_id
                        print(f"Timeout waiting for record_id for msg: {msgs[i].hash}")

            # 如果前面没有，就向后面查找
            for i in range(current_index + 1, len(msgs)):
                if msgs[i].is_video:
                    if msgs[i].record_id is not None:
                        return msgs[i].record_id
                    with msgs[i].record_id_condition:
                        print(f"Waiting for record_id to be set for msg: {msgs[i].hash}")
                        max_retry = 3
                        for retry in range(max_retry):
                            if msgs[i].record_id_condition.wait(timeout=10):
                                if msgs[i].record_id is not None:
                                    print(f"Retrieved record_id: {msgs[i].record_id} for msg: {msgs[i].hash}")
                                    return msgs[i].record_id
                        print(f"Timeout waiting for record_id for msg: {msgs[i].hash}")

            # 第一次查找结束后等待5秒，然后进行第二次查找
            print("wait for next search")
            time.sleep(5)

        return None

def md5(text):
    return hashlib.md5(text.encode()).hexdigest()

if __name__ == "__main__":
    #python -m utils.MsgRecords
    import threading
    import time

    # 模拟 WxMsg 类
    class MockWxMsg:
        def __init__(self, content, roomid, sender, msg_type=1):
            self.content = content
            self.roomid = roomid
            self.sender = sender
            self.type = msg_type

        def from_group(self):
            return True

    # 创建消息记录对象
    msg_records = MsgRecords()

    # 模拟消息
    video_msg = MockWxMsg("https://www.bilibili.com/video/1", "room1", "user1")
    video_msg2 = MockWxMsg("https://www.bilibili.com/video/2", "room1", "user1")
    text_msg = MockWxMsg("This is a text message", "room1", "user1", msg_type=1)

    # 线程1：添加视频消息并设置 record_id
    def thread1_func():
        type = 3
        if type == 1:
            #测试最近的recordid
            msg_records.add_msg(video_msg)
            msg_records.set_record_id(video_msg, "111")
            msg_records.add_msg(video_msg2)
            msg_records.set_record_id(video_msg2, "2333")
        if type == 2:
            # 测试延迟id
            msg_records.add_msg(video_msg)
            time.sleep(15)
            msg_records.set_record_id(video_msg, "111")
        if type == 3:
            #消息比视频早来
            time.sleep(5)
            msg_records.add_msg(video_msg)
            time.sleep(3)
            msg_records.set_record_id(video_msg, "111")

    # 线程2：添加文本消息并尝试获取 record_id
    def thread2_func():
        type = 1
        if type == 1:
            msg_records.add_msg(text_msg)
            record_id = msg_records.get_near_record_id(text_msg)

        print(f"Record ID: {record_id}")

    # 启动线程
    thread1 = threading.Thread(target=thread1_func)
    thread2 = threading.Thread(target=thread2_func)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()