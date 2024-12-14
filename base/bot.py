import os
from random import randint
from queue import Empty
from threading import Thread
import time
import logging
import hashlib
from datetime import datetime
import traceback
from api.openaiApi import openaiApi
from base.randomMsg import randomMsg
from utils.MsgRecords import MsgRecords
from config import *
from wcferry.client import Wcf
from wcferry.wxmsg import WxMsg
class bot:
    def __init__(self, log: logging):
        self.wcf = Wcf(debug=True)
        self.wxid = self.wcf.get_self_wxid()
        self.log = log
        self.MsgRecords = MsgRecords()
        self.randomMsg = randomMsg()
        self.oai = openaiApi()
        self.roomid = "44646802384@chatroom"#需要处理消息的roomid
        self.master_ids = [
            "wxid_3zcnbha3j2v922",#xy3
            "wxid_jvoles5bl6522",#hy
            "wxid_s5ruh5lygq9722",#tokisakix
        ]
        # 启用接收消息
        if not self.wcf.enable_receiving_msg():
            self.log.error("启用接收消息失败")
            return
        self.log.info("已启用消息接收，等待消息...")
    def processMsg(self, msg: WxMsg):
        roomid = msg.roomid
        if roomid != self.roomid and msg.from_group():
            return
        #判断发言人是主人
        if msg.sender in self.master_ids:
            #指`令支持
            txt = msg.content
            if "/最近消息" in txt:
                recent_msg = self.MsgRecords.get_recent_msg(self.roomid,self.wcf)
                #判断群
                if msg.from_group():
                    self.send_msg(f"最近消息:\n{recent_msg}", self.roomid)
                else:
                    self.send_msg(f"最近消息:\n{recent_msg}", msg.sender)
                return
            if "/总结" in txt:
                if msg.from_group():
                    recevier = self.roomid
                else:
                    recevier = msg.sender
                # img = f"{img_dir}/load.gif"
                # self.log.info(f"发送表情:{img}")
                # self.wcf.send_file(img, recevier)
                ai_reply = self.summary(False)
                self.send_msg(ai_reply,recevier)
                return
        self.MsgRecords.add_msg(msg,self.wcf)
    def run(self):
        summary_thread = Thread(target=self.summary_thread)
        summary_thread.start()
        while self.wcf.is_receiving_msg():
            try:
                # 从消息队列中获取消息
                msg: WxMsg = self.wcf.get_msg()
                self.log.debug(f"收到消息({msg.type}): {msg.content} 来自 {msg.sender} 在 {msg.roomid}")
                thread = Thread(target=self.processMsg, args=(msg,))
                thread.start()
            except Empty:
                continue
            except Exception as e:
                self.log.error(f"处理消息时发生错误: {e}")
                time.sleep(1)  # 等待一段时间后重试
    def send_msg(self, msg:str, receiver, at_list=""):
        if not msg:
            return
        msg_length = len(msg)
        if msg_length <= 4000:
            status = self.wcf.send_text(f"{msg} {self.randomMsg.random_emoji()}", receiver, at_list)
            if status == 0:
                self.log.info(f"成功回复: {msg} 给 {receiver}")
            else:
                self.log.error(f"回复失败，状态码: {status}")
        else:
            segments = [msg[i:i + 4000] for i in range(0, msg_length, 4000)]
            for segment in segments:
                status = self.wcf.send_text(f"{segment} {self.randomMsg.random_emoji()}", receiver, at_list)
                if status == 0:
                    self.log.info(f"成功发送分段消息: {segment} 给 {receiver}")
                else:
                    self.log.error(f"分段消息发送失败，状态码: {status}")
    #定时总结
    def summary_thread(self):
        while True:
            #1个小时
            time.sleep(60*60)
            ai_reply = self.summary()
            self.send_msg(ai_reply, self.roomid)

    def summary(self,schedule=True):
        self.log.info("开始总结")
        #判断0点-7点不说话
        now = datetime.now()
        if schedule and now.hour < 7 and now.hour >= 0:
            return
        system_prompt = """你是一个中文的群聊总结的助手，你可以为一个微信的群聊记录，提取并总结每个时间段大家在重点讨论的话题内容。

请帮我将给出的群聊内容总结成一个今日的群聊报告，包含不多于10个的话题的总结（如果还有更多话题，可以在后面简单补充）。每个话题包含以下内容：
- 话题名(50字以内，带序号1⃣2⃣3⃣，同时附带热度，以🔥数量表示）
- 参与者(不超过5个人，将重复的人名去重)
- 时间段(从几点到几点)
- 过程(50到200字左右）
- 评价(50字以下，以傲娇的女大学生视角进行毒舌嘲讽或吐槽，如果和“阳。”相关的，则不毒舌嘲讽吐槽。)
- 分割线： ------------

另外有以下要求：
1. 每个话题结束使用 ------------ 分割
2. 使用中文冒号
3. 无需大标题
4. 开始给出本群讨论风格的整体评价，例如活跃、太水、太黄、太暴力、话题不集中、无聊诸如此类

最后总结下今日最活跃的前五个发言者。

用户输入为群聊内容："""
        user_prompt  = self.MsgRecords.get_recent_msg(self.roomid,self.wcf)
        if not user_prompt:
            self.log.error("user_prompt error")
            return
        ai_reply,errmsg = self.oai.chat(system_prompt + user_prompt)
        if not ai_reply:
            self.log.error(f"ai_reply error: {errmsg}")
            return
        return ai_reply
