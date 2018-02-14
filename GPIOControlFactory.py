import RPi.GPIO as GPIO
import time

'''

Object used to interface clients with GPIO control to be able to draw
current from selected solar cells

'''
class GPIOControlFactory(object):
    '''
    Instantiates an identifiable GPIOControlFactory instance

    val: integer to identify the instantiated class
    return: instance of GPIOControlFactory
    '''
    def __init__(self,val):
        self.val = val

    '''
    Setups up the GPIO #PIN as OUT and turns it on
    '''
    def engageGPIO(self, PIN):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN, GPIO.OUT)
        GPIO.output(PIN, GPIO.LOW)
        print("Test started...")

    '''
    Turns off the selected GPIO #PIN
    '''
    def disengageGPIO(self, PIN):
        GPIO.setmode(GPIO.BCM)
        GPIO.output(PIN, GPIO.HIGH)
        GPIO.cleanup()
