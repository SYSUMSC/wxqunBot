# -*- coding: utf-8 -*-
from pystools.PLogger import PLogger

from pathlib import Path

# project_path = Path.cwd().parent
project_path = Path.cwd()
LogPath = Path(project_path, "logs")
log_name = "err.log"

print("项目日志默认目录为：", f"{LogPath}/{log_name}")
log = PLogger(log_folder=LogPath, log_name=log_name).get_logger()

# log = PLogger(log_name=log_name).get_logger()


def oss_progress_callback(consumed_bytes, total_byte):
    log.info(f"上传进度：{consumed_bytes}/{total_byte}  {consumed_bytes / total_byte * 100:.2f}%")
