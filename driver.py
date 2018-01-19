#!/usr/bin/env python2
from threading import Thread
import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

from gpioSwitchThread import *# setup as a package
from ADCThread import *# setup as a package
            
# Setting up threads 
gpioThread = gpioSwitchThread(0)
adcThread = ADCThread(1)

# 10 Second test for Solar Cell Data Acquisition System
gpioThread.start()
adcThread.start()

print('TEST COMPLETE')
