'''
Created on Oct 12, 2018

@author: l0t0y
'''

from labs.module03.TempActuatorEmulator import TempActuatorEmulator
from asyncio.tasks import sleep

TS = TempSensorEmulator(5)
TS.daemon = True

print("Daemon Thread Starting...")
TS.setEnableTempEmulator(True)
TS.start()

while(True):
    sleep(5)
    pass