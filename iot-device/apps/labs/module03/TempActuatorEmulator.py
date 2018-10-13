'''
Created on Oct 12, 2018

@author: l0t0y
'''
from threading import Thread
from labs.common.ActuatorData import ActuatorData
from time import sleep
from labs.module03.SenseHatLedActivator import SenseHatLedActivator

class TempActuatorEmulator(Thread):
    
    senseHatLed = 0
    actuatorData = 0
    message = 0

    def __init__(self):
        Thread.__init__(self)

        self.actuatorData = ActuatorData()
        self.senseHatLed = SenseHatLedActivator()
    
    def processMessage(self):

        if (self.actuatorData.getCommand() == 1):
            self.message = 'Increasing'
            
        if (self.actuatorData.getCommand() == 2):
            self.message = 'Decreasing'
            
        else:
            self.message = 'Error'
        
        self.senseHatLed.setDisplayMessage(self.message)
        
    def run(self):
        while (self.actuatorData.getCommand() != 0):
            print('\n Actuator start working ...')
            self.processMessage()
            