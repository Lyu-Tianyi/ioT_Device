'''
Created on Sep 22, 2018

@author: l0t0y
'''
import os
from datetime import datetime
from _overlapped import NULL
from tensorflow.python.framework.test_ops import none
class SensorData():
    timeStamp = None
    name = 'Not set'
    curValue = None
    avgValue = 0
    minValue = 0
    maxValue = 0
    totValue = 0
    sampleCount = 0
    
    def __init__(self):
        self.timeStamp = str(datetime.now())
        self.curValue=None
        self.minValue=None
        self.maxValue=None
        self.avgValue=None
        self.sampleCount=0
        self.totValue=0
    
    def addValue(self, newVal):
        self.sampleCount += 1
        self.timeStamp = str(datetime.now())
        if (self.curValue == None):
            self.minValue = newVal
            self.maxValue = newVal
            self.avgValue = newVal
            
        self.curValue = newVal
        self.totValue=self.totValue+self.curValue
          
        if (self.curValue < self.minValue):
            self.minValue = self.curValue
        if (self.curValue > self.maxValue):
            self.maxValue = self.curValue
            
        self.avgValue = self.totValue / self.sampleCount
            
    def getAvgValue(self):
        return self.avgValue
    def getMaxValue(self):
        return self.maxValue
    def getMinValue(self):
        return self.minValue
    def getValue(self):
        return self.curValue
    def setName(self, name):
        self.name = name
    def __str__(self):
        customStr = \
        str(self.name + ':' + \
            os.linesep + '\tTime: ' + self.timeStamp + \
            os.linesep + '\tCurrent: ' + str(self.curValue) + \
            os.linesep + '\tAverage: ' + str(self.avgValue) + \
            os.linesep + '\tSamples: ' + str(self.sampleCount) + \
            os.linesep + '\tMin: ' + str(self.minValue) + \
            os.linesep + '\tMax: ' + str(self.maxValue))
        return customStr