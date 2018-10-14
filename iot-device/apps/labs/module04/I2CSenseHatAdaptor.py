'''
Created on Oct 13, 2018

@author: l0t0y
'''

import smbus
import threading
from time import sleep

#from labs.common import ConfigConst

i2cBus = smbus.SMBus(1) # Use I2C bus No.1 on Raspberry Pi3 +
enableControl = 0x2D
enableMeasure = 0x08
accelAddr = 0x1C # address for IMU (accelerometer)
magAddr = 0x6A # address for IMU (magnetometer)
pressAddr = 0x5C # address for pressure sensor
humidAddr = 0x5F # address for humidity sensor
begAddr = 0x28
totBytes = 6
DEFAULT_RATE_IN_SEC = 5

class I2CSenseHatAdaptor(threading.Thread):
    rateInSec = DEFAULT_RATE_IN_SEC
    
    def __init__(self):
        super(I2CSenseHatAdaptor, self).__init__()

        self.initI2CBus()

        
     
    def initI2CBus(self):
        print("Initialize i2c bus and enabling i2c address....")
        i2cBus.write_byte_data(accelAddr,enableControl,enableMeasure)
        i2cBus.write_byte_data(magAddr,enableControl,enableMeasure) 
        i2cBus.write_byte_data(pressAddr,enableControl,enableMeasure)
        i2cBus.write_byte_data(humidAddr,enableControl,enableMeasure)
        
    def displayAccelerometerData(self):
        
        print(i2cBus.read_i2c_block_data(accelAddr,begAddr,6))
    
    def displayMagnetometerData(self):
        
        print(i2cBus.read_i2c_block_data(magAddr,begAddr,6))
    
    def displayPressureData(self):
        
        print(i2cBus.read_i2c_block_data(pressAddr,begAddr,1))
    
    def displayHumidityData(self):
        
        print(i2cBus.read_i2c_block_data(humidAddr,begAddr,1))
        
# TODO: do the same for the magAddr, pressAddr, and humidAddr
# NOTE: Reading data from the sensor will look like the following:
#data = i2cBus.read_i2c_block_data({sensor address}, {starting read address}, {number of bytes})
    def run(self):
        while True:
                # NOTE: you must implement these methods
                self.displayAccelerometerData()
                self.displayMagnetometerData()
                self.displayPressureData()
                self.displayHumidityData()
                sleep(self.rateInSec)         
                
                
                
i2c=I2CSenseHatAdaptor()
i2c.daemon=True
i2c.start()



while True:
    pass               
                
                