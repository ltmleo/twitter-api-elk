import os, configparser

class System:
    def __init__(self, group):
        self.WORKDIR=os.path.dirname(os.path.abspath(__file__))
        config = configparser.ConfigParser()
        config.read(f"{self.WORKDIR}/../project.properties")
        self.ENV=dict(config.items(group))
