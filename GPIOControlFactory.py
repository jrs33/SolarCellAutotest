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
    This function simulates the cell selection sets GPIO14 as the pin
    to engage the transistor. Identical to a binary select for one cell

    TODO: MUST BE ALTERED TO INTERFACE WITH MULTIPLE CELLS. Will need
    to replace with a 3-bit binary to interfaec 8 cells with a relay
    '''
    def cellSelect(self):
        GPIO.setmode(GPIO.BCM)
        return 14

    '''
    Setups up the GPIO #PIN as OUT and turns it on
    '''
    def engageGPIO(self, PIN):
        GPIO.setup(PIN, GPIO.OUT)
        GPIO.output(PIN, True)

    '''
    Turns off the selected GPIO #PIN
    '''
    def disengageGPIO(self, PIN):
        GPIO.output(PIN, False)
        GPIO.cleanup()
