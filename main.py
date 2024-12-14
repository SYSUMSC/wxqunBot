import logging
import sys
from base.bot import bot  # 导入 bot 类
import os
from utils.logger import log

def main():
    chatbot = bot(log)  # 实例化 bot 类

    # 检查 bot 是否成功初始化
    if not chatbot.wcf.is_receiving_msg():
        logging.error("Bot 初始化失败，无法接收消息")
        return

    logging.info("注册退出处理函数")
    atexit.register(on_exit)
    logging.info("启动主任务")
    chatbot.run()

if __name__ == "__main__":
    main()