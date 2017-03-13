# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 20:50:40 2017

@author: jklei
"""

import serial
    
myPort = serial.Serial('/dev/ttyUSB0', 115200, timeout = 10)

while(True):
    myPort.write("Serial Test")
myPort.close()