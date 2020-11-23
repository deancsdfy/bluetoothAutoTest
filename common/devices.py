import subprocess,platform
from utils.config import Config
from  utils.logger import Logger

logger = Logger(logger='devices').getlog()

class Devices():
    def __init__(self):
        self.c = Config()
    # 封装adb
    def shell(self,args):
        sys = platform.system()
        if sys == 'Windows':
            cmd = 'adb shell \"%s\"' % (str(args))
        elif sys == 'Darwin':
            cmd = 'adb shell %s' % (str(args))
        else:
            raise RuntimeError('本工具暂不支持当前系统！')
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 获取设备型号
    def getDevicesName(self):
        devicesName = self.shell('getprop ro.product.model').stdout.read().decode().strip()
        return devicesName

    # 获取设备SN
    def getDevicesSN(self):
        devicesSN = self.shell('getprop ro.serialno').stdout.read().decode().strip()
        return devicesSN

    # 判断蓝牙是否开启
    def isBluetoothStatus(self):
        pi = self.shell('settings get global bluetooth_on')
        result = pi.stdout.read().decode().strip()
        if  result == '1':
            return True
        elif result == '0':
            return False
        else:
            raise RuntimeError('蓝牙状态获取失败')

    def openBluetoothSet(self):
        self.shell('am start -a android.settings.BLUETOOTH_SETTINGS')
        logger.info('打开蓝牙系统设置页面')

    # 获取屏幕右边部分区域坐标
    def getDisplayRightRect(self):
        result = self.shell('wm size').stdout.read().decode().strip()
        w = int(result.split()[2].split('x')[0])
        h = int(result.split()[2].split('x')[1])
        Rect = (w/2,0,w,h)
        return Rect

    def getBTswitchPx(self):
        devicesName = self.getDevicesName()
        c = Config()
        px = c.get('blueSwitchPx').get(devicesName)
        # str转typle
        px = eval(repr(px).replace('\'',''))
        return px
    def installStannisDemo(self):
        pack_path = self.c.pack_path
        os.system('adb install {}'.format(pack_path))
        print('1')

if __name__ == '__main__':
    d = Devices()
    print(d.installStannisDemo())




