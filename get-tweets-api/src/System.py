import os, configparser, logging
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.handler import LogstashFormatter
class Log:
    def __init__(self):
        self.logger = logging.getLogger("logstash")
        self.logger.setLevel(logging.INFO)
        try:       
            host = os.environ["LOGSTASH_HOST"]
        except:
            host = "localhost"
        try:
            port = int(os.environ["LOGSTASH_PORT"])
        except:
            port = 5044
        handler = AsynchronousLogstashHandler(
            host=host, 
            port=port, 
            ssl_enable=False, 
            ssl_verify=False,
            database_path='')

        formatter = LogstashFormatter()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.info("Init logger")

    def error(self, message):
        self.logger.error({"app": "save-tweets", "message": message})
        print({"level": "error", "message": message})

    def info(self, message):
        self.logger.info({"app": "save-tweets", "message": message})
        print({"level": "info", "message": message})

    def warning(self, message):
        self.logger.warning({"app": "save-tweets", "message": message})
        print({"level": "warning", "message": message})

    def debug(self, message):
        self.logger.debug({"app": "save-tweets", "message": message})
        print({"level": "debug", "message": message})

