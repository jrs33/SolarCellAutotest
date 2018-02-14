import RPi.GPIO as GPIO
import time
from TestingConstants import TestingConstants

'''

Object used to interface the testing logic with the EDS
power supply

'''
class EDSControlFactory(object):
    '''
    Instantiates an identifiable EDSControlFactory instance
        val: integer to id the class
        return: instance of an EDSControlFactory
    '''
    def __init__(self, val):
        self.val = val
        self.constants = TestingConstants()

    def engagePowerSupplyAndClean(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.constants.EDS_TRIGGER_PIN, GPIO.OUT)
        GPIO.output(self.constants.EDS_TRIGGER_PIN, GPIO.HIGH)

        cleaningTime = 120
        print("Cleaning the cells...")
        time.sleep(cleaningTime)

    def disengagePowerSupply(self):
        GPIO.output(self.constants.EDS_TRIGGER_PIN, False)
        GPIO.cleanup()

