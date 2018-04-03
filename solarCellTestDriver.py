#import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import dht11
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
    cellDictionary = {12:"1", 16:"2", 20:"3", 21:"4"}

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

    dhtResult = getTemperatureAndHumidity()

    if dhtResult is not None:
        temperature = dhtResult.temperature
        humidity = dhtResult.humidity
        #transporter.transportToUSB(ratio,selectedCell,str(datetime.datetime.now()))
        #transporter.transportToBufferFile(ratio,selectedCell,str(datetime.datetime.now()))
        transporter.transportToDB(ratio,cellDictionary[selectedCell],"nil","nil",temperature,humidity)
    else:
        print("NO TEMP")

    return ratio

'''
This function returns 
'''
def getTemperatureAndHumidity():
    GPIO.setmode(GPIO.BCM)
    instance = dht11.DHT11(pin=17)
    result = instance.read()

    print(result)
    if result.is_valid():
        return result
