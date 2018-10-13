'''
Created on Oct 12, 2018

@author: l0t0y
'''
from threading import Thread
from time import sleep
from labs.common.SensorData import SensorData
from labs.common.ActuatorData import ActuatorData
from SenseHat import SenseHat
from labs.common.ConfigUtil import ConfigUtil
from labs.common.ConfigConst import ConfigConst
from labs.module03.Connector import Connector

class TempSensorAdaptor(Thread):

    curTemp = 0
    updateTime = 0
    rateInSec = 0
    sensorData = 0
    senseHat = 0
    connector = 0
    alertDiff = 0
    senseHatLed = 0
    actuatorData = 0

    def __init__(self, rateInSec):
        Thread.__init__(self)
        self.highVal = 30
        self.lowVal = 0
        self.updateTime = 2
        self.rateInSec = rateInSec
        self.senseHat = SenseHat()
        self.sensorData = SensorData()
        self.actuatorData = ActuatorData()
        self.connector = Connector()
        self.alertDiff = 10
        
        self.config = ConfigUtil('D:/git/repository/iot-device/apps/data/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        print('Configuration data...\n' + str(self.config))

    def getCurrValue(self):

        return self.currValue

    def setEnableTempEmulator(self, flag):
        self.enableTempEmulator = flag

    def run(self):
        while True:
            self.curTemp = self.senseHat.get_temperature()
            self.sensorData.addValue(self.curTemp)
            print('\n--------------------')
            print('New sensor readings: \n')
            print(' ' + str(self.sensorData))
            
            print('New actuator readings: \n')
            print(' ' + str(self.actuatorData))

            if (abs(self.curTemp - float(self.config.getProperty(ConfigConst.CONSTRAINED_DEVICE,ConfigConst.TEMP_KEY))) > self.alertDiff):
                print('\n Current temp exceeds average by > ' + str(self.alertDiff) + '. Triggering alert...')
                self.connector.publishMessage('Exceptional sensor and actuator data [test]', self.sensorData + self.actuatorData)
                print('\n Actuator activating...')
                if (self.curTemp > float(self.config.getProperty(ConfigConst.CONSTRAINED_DEVICE,ConfigConst.TEMP_KEY))):
                    self.actuatorData.addValue(1, abs(self.curTemp - self.config.getProperty(ConfigConst.CONSTRAINED_DEVICE,ConfigConst.TEMP_KEY)))
                else:
                    self.actuatorData.addValue(2, abs(self.curTemp - self.config.getProperty(ConfigConst.CONSTRAINED_DEVICE,ConfigConst.TEMP_KEY)))
                # LED Display
                #self.senseHatLed.displayMsg(abs(self.curTemp - self.config.getProperty(ConfigConst.CONSTRAINED_DEVICE,ConfigConst.TEMP_KEY)))
                sleep(self.rateInSec)
                
            else:
                self.actuatorData.addValue(0, 0)
            
            
            
        sleep(self.updateTime)