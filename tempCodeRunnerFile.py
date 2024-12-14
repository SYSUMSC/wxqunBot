
from utils.logger import log

def main():
    chatbot = bot(log)  # 实例化 bot 类

    # 检查 bot 是否成功初始化
    if not chatbot.wcf.is_receiving_msg():
        logging.error("Bot 初始化失败，无法接收消息")
        return

    logging.info("启动主任务")
    chatbot.run()

if __name__ == "__main__":
    main()