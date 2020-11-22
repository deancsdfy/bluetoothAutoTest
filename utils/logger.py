#_*_coding:utf-8_*_
import logging
import os.path,sys
import time


class Logger(object):
    def __init__(self,logger):
        '''
        将日志保存到指定的路径文件中
        指定日志的级别，以及调用文件
        '''

        #创建logger文件
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handle，用来写入日志文件
        now = time.strftime("%Y-%m-%d_%H")
        BASE_PATH = os.path.split(os.path.dirname(__file__))[0]
        log_path = os.path.join(BASE_PATH,'./logs/')
        log_name = log_path+now+'.log'

        filehandle = logging.FileHandler(log_name,encoding="utf-8")
        filehandle.setLevel(logging.INFO)

        #创建一个handle，用来输入日志到控制台
        controlhandle = logging.StreamHandler()
        controlhandle.setLevel(logging.INFO)

        #将输出的hangdle格式进行转换
        formatter = logging.Formatter('%(asctime)s[%(name)s][ %(funcName)s]%(levelname)s-%(message)s')
        filehandle.setFormatter(formatter)
        controlhandle.setFormatter(formatter)

        #给logger添加handle
        self.logger.addHandler(filehandle)
        self.logger.addHandler(controlhandle)

    def getlog(self):
        return self.logger