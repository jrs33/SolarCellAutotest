from threading import Thread
import time
import RPi.GPIO as GPIO

class gpioSwitchThread(Thread):

    '''
    This function instantiates the GPIO thread to engage the switching mechanism
    '''
    def __init__(self, val):

        Thread.__init__(self)
        self.val = val

    '''
    This function simulates the cell selection sets GPIO14 as the pin
    '''
    def cellSelect(self):
        GPIO.setmode(GPIO.BCM)
        return 14
        

    '''
    This function creates the GPIO mapping and simulates an event-driven input from the website to conduct a test
    '''
    def switchMechanism(self, PIN):

        GPIO.setup(PIN, GPIO.OUT)

        GPIO.output(PIN, True)

        time.sleep(10)
        GPIO.output(PIN, False)
        GPIO.cleanup()

    '''
    Initiates the GPIO Thread to select a corresponding GPIO pin to initiate the PCB switch
    '''
    def run(self):

        PIN  = self.cellSelect()
        self.switchMechanism(PIN)
        
