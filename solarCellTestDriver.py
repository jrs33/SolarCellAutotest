import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
#import dht11
import datetime

from GPIOControlFactory import *
from ADCControlFactory import *
from DataTransportFactory import *
from EDSControlFactory import *

'''
This is a function that contains the logic
for our EDS tests. The tests go as follows:

1) Run test on selected cell without the EDS running
2) Record the data from this test
3) Pause the test and turn on the EDS for 2 minutes
4) Turn off the EDS
5) Repeat 1 & 2
6) Compare the ratios of before and after cleaning and
store various data locally and remotely 
'''
def runEDSTest(selectedCell):
    gpio = GPIOControlFactory(0)
    adc = ADCControlFactory(0)
    transporter = DataTransportFactory(0)
    eds = EDSControlFactory(0)

    # Step 1 and 2
    GPIO.setmode(GPIO.BCM)
    gpio.engageGPIO(selectedCell)
    try:
        averagePreClean = adc.gatherADCData()
    except ValueError as error:
        return repr(error)
    gpio.disengageGPIO(selectedCell)

    # Step 3
    eds.engagePowerSupplyAndClean()
    eds.disengagePowerSupply()

    # Step 4
    gpio.engageGPIO(selectedCell)
    try:
        averagePostClean = adc.gatherADCData()
    except ValueError as error:
        return repr(error)
    gpio.disengageGPIO(selectedCell)

    # Step 5 ADD IN DATE AND TIME ISOLATION AND TEMPERATURE AND HUMIDITY
    ratio = 0
    if averagePreClean != 0:
        ratio = averagePostClean/averagePreClean
    tempHumidList = getTemperatureAndHumidity()
    temperature = tempHumidList[0]
    humidity = tempHumidList[1]

    transporter.transportToUSB(ratio,selectedCell,str(datetime.now()))
    transporter.transportToBufferFile(ratio,selectedCell,str(datetime.now()))
    transporter.transportToDB(ratio,selectedCell,str(date.today()),str(time.time()))

    return ratio

'''
This function returns 
'''
def getTemperatureAndHumidity():
    instance = dht11.DHT11(pin=17)
    result = instance.read()
    tempHumidList = []
    if result.is_valid():
        tempHumidList.append(result.temperature)
        tempHumidList.append(result.humidity)
    return tempHumidList
