'''
Created on Sep 15, 2018

@author: l0t0y
'''
from threading import Thread
import psutil
from time import sleep

class SystemPerformanceAdaptor(Thread):
    '''
    classdocs
    '''


    def __init__(self):
        Thread.__init__(self)
        
        self.rateInSec=2
    
    def run(self):
        while True:
            #if self.enableAdaptor:
                print('\n--------------------')
                print('New system performance readings:')
                print(' ' + str(psutil.cpu_stats()))
                print(' ' + str(psutil.virtual_memory()))

                sleep(self.rateInSec)


sysPerfAdaptor = SystemPerformanceAdaptor()
sysPerfAdaptor.daemon = True
print("Starting system performance app daemon thread...")

sysPerfAdaptor.start()
while (True):
    sleep(5)
    pass


