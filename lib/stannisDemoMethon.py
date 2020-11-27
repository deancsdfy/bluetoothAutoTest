from time import sleep
from common.systemMethon import System
from utils.config import Config

class Stannis():
    def __init__(self):
        self.dr = System().connectDevices()
        self.c = Config()

    def start(self):
        start_btn_xpath = self.c.get('stannisDemoInfo').get('xpath').get('start_btn')
        self.dr(resourceId=start_btn_xpath).click()
        sleep(1)
        print(self.dr(resourceId=start_btn_xpath).get_text())

if __name__ == '__main__':
    s = Stannis()
    s.start()
