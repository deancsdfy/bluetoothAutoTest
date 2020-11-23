# -*- coding:utf-8 -*-
"""
读取配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""

import os,sys
BASE_PATH = os.path.split(os.path.dirname(__file__))[0]
sys.path.append(BASE_PATH)
from utils.file_read import YamlReader

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
BASE_PATH = os.path.split(os.path.dirname(__file__))[0]
DATA_PATH = os.path.join(BASE_PATH, 'data','data.yaml')
PACK_PATH = os.path.join(BASE_PATH,'data','StannisDemo.apk')
LOG_PATH = os.path.join(BASE_PATH, 'logs')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
SCREENSHOTS_PATH = os.path.join(BASE_PATH,"screenshots",'')
CASE_PATH = os.path.join(BASE_PATH,'case','case.yaml')
# INTERFACE_PATH = os.path.join(BASE_PATH,'test','JieKou','interface.yaml')
# EXE_PATH = os.path.join(BASE_PATH,'test','Autolt','test1.jpg')
# EXCEL_PATH = os.path.join(BASE_PATH,'test','sqlconf','')

class Config():
    def __init__(self, config=DATA_PATH,pack_path=PACK_PATH,case_data = CASE_PATH,screenshot = SCREENSHOTS_PATH):
        self.config = YamlReader(config).data
        self.pack_path = pack_path
        # self.case_data = YamlReader(case_data).data
        # self.interface_data = YamlReader(interface_data).data
        # self.exe_ptah = EXE_PATH
        # self.screen_shot = screenshot
        # self.excel_pt = excel


    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """

        return self.config[index].get(element)

    def get_case_data(self,element,index = 0):
        return self.case_data[index].get(element)
    
# if __name__ == "__main__":
#     c = Config()
#     print(c.get('blueCheckBoxXpath').get('Redmi Note 3'))