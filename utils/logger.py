from loguru import logger

# 配置日志记录
logger.add("logs/app.log", rotation="500 MB", retention="10 days", level="INFO")

# 你可以根据需要添加更多的日志格式化选项
logger.add("logs/error.log", level="ERROR", rotation="10 MB", retention="10 days")

# 导出 logger 对象
log = logger