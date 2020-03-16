import os, configparser, logging
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.handler import LogstashFormatter
class System:
    def __init__(self, group):
        self.WORKDIR=os.path.dirname(os.path.abspath(__file__))
        config = configparser.ConfigParser()
        config.read(f"{self.WORKDIR}/../project.properties")
        self.ENV=dict(config.items(group))

class Log:
    def __init__(self):
        self.logger = logging.getLogger("logstash")
        self.logger.setLevel(logging.ERROR)        

        handler = AsynchronousLogstashHandler(
            host='your-logstash-host', 
            port="8080", 
            ssl_enable=True, 
            ssl_verify=False,
            database_path='')

        formatter = LogstashFormatter()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def error(self, message):
        self.logger.error(f"python-logstash-async: {message}")
        print(f"ERROR: {message}")

    def info(self, message):
        self.logger.info(f"python-logstash-async: {message}")
        print(f"INFO: {message}")

    def warning(self, message):
        self.logger.warning(f"python-logstash-async: {message}")
        print(f"WARNING: {message}")

    def debug(self, message):
        self.logger.debug(f"python-logstash-async: {message}")
        print(f"DEBUG: {message}")

