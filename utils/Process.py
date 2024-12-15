import time
import os
from datetime import datetime, timedelta

def clean_tmp(tmppath):
    """定时清理一天前临时文件"""
    try:
        while True:
            # 获取当前时间
            now = datetime.now()
            # 计算一天前的时间
            one_day_ago = now - timedelta(days=1)

            # 遍历临时目录中的文件
            for root, dirs, files in os.walk(tmppath):
                for file in files:
                    file_path = os.path.join(root, file)
                    # 获取文件的最后修改时间
                    file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                    # 如果文件的最后修改时间早于一天前，则删除文件
                    if file_mtime < one_day_ago:
                        os.remove(file_path)
                        print(f"删除文件: {file_path}")

            # 每小时清理一次
            time.sleep(3600)  # 3600秒 = 1小时
    except Exception as e:
        print(f"清理临时文件时出错: {e}")

