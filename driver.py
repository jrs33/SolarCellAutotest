#!/usr/bin/env python2
import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

from GPIOControlFactory import *
from ADCControlFactory import *
from DataTransportFactory import *

'''
This is an abstracted function to run the logic
for our EDS tests. The tests go as follows:

1) Run test on selected cell without the EDS running
2) Record the data from this these locally and remotely
3) Pause the test and turn on the EDS for 2 minutes
4) Turn off the EDS
5) Repeat 1 & 2
6) Compare the ratios of before and after cleaning to get
EDS effectiveness
'''
def runEDSTest():
    gpio = GPIOControlFactory(0)
    adc = ADCControlFactory(0)
    transporter = DataTransportFactory(0)

    # Step 1
    selectedCell = gpio.cellSelect()
    gpio.engageGPIO(selectedCell)
    average = adc.gatherADCData()
    gpio.disengageGPIO(selectedCell)

    # Step 2
    transporter.transportToUSB(average)

    # Step 3
    

runEDSTest()
