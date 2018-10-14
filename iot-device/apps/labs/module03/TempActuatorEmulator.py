'''
Created on Oct 12, 2018

@author: l0t0y
'''
from threading import Thread
from labs.common.ActuatorData import ActuatorData
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
        
        if (self.actuatorData.getCommand() == 0):
            self.message = 'Stay'

        elif (self.actuatorData.getCommand() == 1):
            self.message = 'Increasing'
            self.senseHatLed.setDisplayMessage(self.message)
            
        elif (self.actuatorData.getCommand() == 2):
            self.message = 'Decreasing'
            self.senseHatLed.setDisplayMessage(self.message)
            
        else:
            self.message = 'Error'
            self.senseHatLed.setDisplayMessage(self.message)
    
    
    def update(self,actuatorData): 
        self.actuatorData.updateData(actuatorData)
        
        
    def run(self):
        while True:
            while(self.actuatorData.getCommand() != 0):
            
                self.processMessage(self.actuatorData)
                
                
    
        
        
        
