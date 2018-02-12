import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

from datetime import datetime

from GPIOControlFactory import *
from ADCControlFactory import *
from DataTransportFactory import *
from EDSControlFactory import *

'''
This is an abstracted function to run the logic
for our EDS tests. The tests go as follows:

1) Run test on selected cell without the EDS running
2) Record the data from this test
3) Pause the test and turn on the EDS for 2 minutes
4) Turn off the EDS
5) Repeat 1 & 2
6) Compare the ratios of before and after cleaning and
store data locally and remotely 
'''
def runEDSTest(selectedCell):
    gpio = GPIOControlFactory(0)
    adc = ADCControlFactory(0)
    transporter = DataTransportFactory(0)
    eds = EDSControlFactory(0)

    # Step 1 and 2
    GPIO.setmode(GPIO.BCM)
    gpio.engageGPIO(selectedCell)
    averagePreClean = adc.gatherADCData()
    gpio.disengageGPIO(selectedCell)

    # Step 3
    eds.engagePowerSupplyAndClean()
    eds.disengagePowerSupply()

    # Step 4
    gpio.engageGPIO(selectedCell)
    averagePostClean = adc.gatherADCData()
    gpio.disengageGPIO(selectedCell)

    # Step 5
    ratio = 0
    if averagePreClean != 0:
        ratio = averagePostClean/averagePreClean
    transporter.transportToUSB(ratio,selectedCell,str(datetime.now()))

    return ratio
