import logging.handlers

class GetLog(object):
    __logger = None

    @classmethod
    def get_log(cls):
        if cls.__logger is None:
            #获取日志器
            cls.__logger = logging.getLogger()
            #修改默认级别
            cls.__logger.setLevel(logging.INFO)
            file = "./logging/hmtt.log"
            #获取处理器
            th = logging.handlers.TimedRotatingFileHandler(filename=file,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            #获取格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            #将格式器添加到处理器1
            th.setFormatter(fm)
            #将处理器添加到日志器
            cls.__logger.addHandler(th)
        return cls.__logger