import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import dht11
import time

from GPIOControlFactory import *
from ADCControlFactory import *
from DataTransportFactory import *
from EDSControlFactory import *

'''
This is a function that contains the logic
for our EDS tests. The tests go as follows:

1) Run test on selected cell, or all cells if bulk is True, without the EDS running IF humidity is 30-50%
2) Record the data from this test
3) Pause the test and turn on ALL EDS's for 2 minutes
4) Turn off the EDS
5) Repeat 1 & 2
6) Compare the ratios of before and after cleaning and
store various data locally and remotely 
'''
def runEDSTest(selectedCell, bulk=False):
    if(not checkHumidityPreconditions()):
        return 'Humidity not in 30-50 range; aborting test'

    cellDictionary = {12:"1", 16:"2", 20:"3", 21:"4"}

    transporter = DataTransportFactory(0)
    eds = EDSControlFactory(0)

    # Gather pre-cleaning averages
    if(not bulk):
        averagePreClean = engageAndGatherCurrentAverage(selectedCell)
    else:
        averagesPreClean = 4 * [0]
        for index, value in enumerate(cellDictionary.keys()):
            print(str(value) + str(averagesPreClean))
            averagesPreClean[index] = engageAndGatherCurrentAverage(value)
            if(isinstance(averagesPreClean[index],str)):
                return averagesPreClean[index]

    # Engage ALL EDS modules
    eds.engagePowerSupplyAndClean()
    eds.disengagePowerSupply()

    # Gather post-cleaning averages
    if(not bulk):
        averagePostClean = engageAndGatherCurrentAverage(selectedCell)
    else:
        averagesPostClean = 4 * [0]
        for index, value in enumerate(cellDictionary.keys()):
            print(str(value) + str(averagesPostClean))
            averagesPostClean[index] = engageAndGatherCurrentAverage(value)
            if(isinstance(averagesPostClean[index],str)):
                return averagesPostClean[index]

    # Calculate ratios, get dht11 results and store data
    if(not bulk):
        ratio = 0
        if(averagePreClean != 0):
            ratio = averagePostClean/averagePreClean
        else:
            ratio = 0
    else:
        ratioArray = 4 * [0]
        for index, value in enumerate(averagesPreClean):
            if(averagesPreClean[index] != 0):
                ratioArray[index] = averagesPostClean[index]/averagesPreClean[index]

    dhtResult = getTemperatureAndHumidity()

    if dhtResult is not None:
        temperature = dhtResult.temperature
        humidity = dhtResult.humidity

        if(not bulk):
            transporter.transportToBufferFile(ratio,selectedCell,time.strftime("%x"),time.strftime("%X"),temperature,humidity)
            transporter.transportToDB(ratio,cellDictionary[selectedCell],time.strftime("%x"),time.strftime("%X"),temperature,humidity)
        else:
            for index, value in enumerate(cellDictionary.keys()):
                transporter.transportToBufferFile(ratioArray[index],value,time.strftime("%x"),time.strftime("%X"),temperature,humidity)
                transporter.transportToDB(ratioArray[index],value,time.strftime("%x"),time.strftime("%X"),temperature,humidity)
    else:
        if(not bulk):
            transporter.transportToBufferFile(ratio,selectedCell,time.strftime("%x"),time.strftime("%X"))
            transporter.transportToDB(ratio,cellDictionary[selectedCell],time.strftime("%x"),time.strftime("%X"),0,0)
        else:
            for index, value in enumerate(cellDictionary.keys()):
                transporter.transportToBufferFile(ratioArray[index],value,time.strftime("%x"),time.strftime("%X"))
                transporter.transportToDB(ratioArray[index],value,time.strftime("%x"),time.strftime("%X"),0,0)

    if(not bulk):
        return ratio
    else:
        return ratioArray

'''
This utility turns on the gpio for the selected cell and returns the average current for twenty measurements
'''
def engageAndGatherCurrentAverage(selectedCell):
    GPIO.setmode(GPIO.BCM)
    gpio = GPIOControlFactory(0)
    adc = ADCControlFactory(0)

    gpio.engageGPIO(selectedCell)
    try:
        averageCurrent = adc.gatherADCData()
        gpio.disengageGPIO(selectedCell)
        return averageCurrent
    except ValueError as error:
        gpio.disengageGPIO(selectedCell)
        return repr(error)

'''
This function returns temperature and humidity from the dht11 sensor
'''
def getTemperatureAndHumidity():
    GPIO.setmode(GPIO.BCM)
    instance = dht11.DHT11(pin=17)
    result = instance.read()

    print(result)
    if result.is_valid():
        return result

def checkHumidityPreconditions():
    dhtResult = getTemperatureAndHumidity()

    if dhtResult is not None:
        humidity = dhtResult.humidity
        if(humidity >= 30 and humidity <= 50):
            return True
        else:
            print('Humidity not in 30-50 range; aborting test')
            return False
    else:
        return False
