'''
Created on Sep 22, 2018

@author: l0t0y
'''

from threading import Thread
from random import uniform
from time import sleep
from labs.common.SensorData import SensorData
from labs.module02.SmtpClientConnector import SmtpClientConnector


class TempSensorEmulator(Thread):

    curTemp = 0
    highVal = 0
    lowVal = 0
    enableTempEmulator = False
    updateTime = 0
    rateInSec = 0
    sensorData = 0
    connector = 0
    alertDiff = 0

    def __init__(self, rateInSec):
        Thread.__init__(self)
        self.highVal = 30
        self.lowVal = 0
        self.updateTime = 2
        self.rateInSec = rateInSec
        self.sensorData = SensorData()
        self.connector = SmtpClientConnector()
        self.alertDiff = 10

    def getCurrValue(self):

        return self.currValue

    def setEnableTempEmulator(self, flag):
        self.enableTempEmulator = flag

    def run(self):
        while True:
            if self.enableTempEmulator:
                self.sensorData.setName('Temperature')
                self.curTemp = uniform(float(self.lowVal), float(self.highVal))
                self.sensorData.addValue(self.curTemp)
                print('\n--------------------')
                print('New sensor readings: \n')
                print(' ' + str(self.sensorData))

                if (abs(self.curTemp - self.sensorData.getAvgValue()) >= self.alertDiff):
                    print('\n Current temp exceeds average by > ' + str(self.alertDiff) + '. Triggering alert...')
                    self.connector.publishMessage('Exceptional sensor data [test]', self.sensorData)
                    sleep(self.rateInSec)

            sleep(self.updateTime)
