import RPi.GPIO as GPIO
import time
from TestingConstants import TestingConstants

'''

Object used to interface the Pi with the EDS
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
        self.cleaningTime = 120 #2 minutes

    def engagePowerSupplyAndClean(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.constants.EDS_TRIGGER_PIN, GPIO.OUT)
        GPIO.output(self.constants.EDS_TRIGGER_PIN, GPIO.HIGH)

        print("Cleaning the cells...")
        time.sleep(self.cleaningTime)

    def disengagePowerSupply(self):
        GPIO.output(self.constants.EDS_TRIGGER_PIN, False)
        GPIO.cleanup()

