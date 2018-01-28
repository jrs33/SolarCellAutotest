#!/usr/bin/env python2
import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

from GPIOControlFactory import *
from ADCControlFactory import *
from DataTransportFactory import *

def runEDSTest():
    gpio = GPIOControlFactory(0)
    adc = ADCControlFactory(0)
    transporter = DataTransportFactory(0)

    selectedCell = gpio.cellSelect()
    gpio.engageGPIO(selectedCell)
    average = adc.gatherADCData()
    gpio.disengageGPIO(selectedCell)

    transporter.transportToUSB(average)

    return average

runEDSTest()
