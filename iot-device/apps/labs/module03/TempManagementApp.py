'''
Created on Oct 12, 2018

@author: l0t0y
'''

from labs.module03.TempActuatorEmulator import TempActuatorEmulator
from labs.module03.TempSensorAdaptor import TempSensorAdaptor
from asyncio.tasks import sleep

TSA = TempSensorAdaptor(5)
TSA.daemon = True

TAE = TempActuatorEmulator()
TAE.daemon = True

print("Daemon Thread Starting...")
TSA.start()
TAE.start()

while(True):
    sleep(5)
    pass