# 封装了一些系统层级的操作方法
import uiautomator2
from time import sleep
from  utils.logger import Logger
from common.common import Devices

logger = Logger(logger='systemMethon').getlog()

class System():
    def __init__(self):
        self.d = Devices()

    def connectDevices(self):
        devicesSN = self.d.getDevicesSN()
        self.dr = uiautomator2.connect(devicesSN)
        logger.info('sn：{} 手机连接成功'.format(devicesSN))
        return self.dr


    def killAllApp(self):
        self.dr.app_stop_all()
        logger.info('后台清理成功')

    def showNotification(self):
        self.dr.open_notification()
        logger.info('下拉通知栏成功')

    def hideNotification(self):
        self.dr.swipe_ext("up", scale=0.5, box=self.d.getDisplayRightRect())
        logger.info('收起通知栏成功')

    def openBluetooth(self):
        bluetoothStatusb = self.d.isBluetoothStatus()
        if bluetoothStatusb == True:
            logger.info('蓝牙已开启')
        elif bluetoothStatusb == False:
            self.showNotification()
            sleep(1)
            self.dr.click(*self.d.getBTswitchPx())
            logger.info('点击蓝牙开关')
            sleep(1)
            if self.d.isBluetoothStatus() == True:
                logger.info('蓝牙已开启')
            else:
                logger.error('蓝牙开启失败')
            self.hideNotification()

    def closeBluetooth(self):
        bluetoothStatusb = self.d.isBluetoothStatus()
        if bluetoothStatusb == False:
            logger.info('蓝牙已关闭')
        elif bluetoothStatusb == True:
            self.showNotification()
            sleep(1)
            self.dr.click(*self.d.getBTswitchPx())
            logger.info('点击蓝牙开关')
            sleep(1)
            if self.d.isBluetoothStatus() == False:
                logger.info('蓝牙已关闭')
            else:
                logger.error('蓝牙关闭失败')

    def openStannisDemo(self):
        self.dr.app_start('com.kwai.video.stannisdemo')
        logger.info('启动stannisDemo')

    def closeStannisDemo(self):
        self.dr.app_stop('com.kwai.video.stannisdemo')
        logger.info('结束stannisDemo')

# if __name__ == '__main__':
#     system = System()
#     system.connectDevices()
#     # system.killAllApp()
#     system.openBluetooth()