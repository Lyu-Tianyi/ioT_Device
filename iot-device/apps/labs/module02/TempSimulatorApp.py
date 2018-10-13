'''
Created on Sep 22, 2018

@author: l0t0y
'''

from labs.module02.TempSensorEmulator import TempSensorEmulator
from time import sleep

TS = TempSensorEmulator(5)
TS.daemon = True

print("Daemon Thread Starting...")
TS.setEnableTempEmulator(True)
TS.start()

while(True):
    sleep(5)
    pass






    
    
