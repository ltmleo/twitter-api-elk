import os, configparser, logging
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.handler import LogstashFormatter
class Log:
    def __init__(self):
        self.logger = logging.getLogger("logstash")
        self.logger.setLevel(logging.INFO)        
        host = os.environ["LOGSTASH_HOST"]
        port = int(os.environ["LOGSTASH_PORT"])
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
        self.logger.error(f"get-tweets-api: {message}")
        print(f"ERROR: {message}")

    def info(self, message):
        self.logger.info(f"get-tweets-api: {message}")
        print(f"INFO: {message}")

    def warning(self, message):
        self.logger.warning(f"get-tweets-api: {message}")
        print(f"WARNING: {message}")

    def debug(self, message):
        self.logger.debug(f"get-tweets-api: {message}")
        print(f"DEBUG: {message}")

