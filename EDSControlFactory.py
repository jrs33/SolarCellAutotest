import RPi.GPIO as GPIO
import time

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

    def engagePowerSupplyAndClean(self):
        PIN = 22
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN, GPIO.OUT)
        GPIO.output(PIN, True)

        cleaningTime = 120
        time.sleep(120)

    def disengagePowerSupply(self):
        GPIO.output(22, False)
        GPIO.cleanup()

