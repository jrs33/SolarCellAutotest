import time
import RPi.GPIO as GPIO

'''
This function simulates the cell selection
'''
def cellSelect():
    GPIO.setmode(GPIO.BOARD)

    pinNum = input('Simulates the cell selection (Enter ): ')
    return 8
    

'''
This function creates the GPIO mapping and simulates an event-driven input from the website to conduct a test
'''
def switchMechanism(PIN):

    GPIO.setup(PIN, GPIO.OUT)

    state = 0
    value = input('Simulate Event Driven Website Input (1=ON, 0=OFF): ')
    print('Running input for 10 seconds to simulate a test')

    while True:

        if int(value) == 0:

            GPIO.output(PIN, False)

        elif int(value) == 1:

            GPIO.output(PIN, True)

        time.sleep(10)
        GPIO.output(PIN, False)
        break

    GPIO.cleanup()

'''
Driver program
'''
def main():

    while True:

        pin = cellSelect()
        switchMechanism(pin)


main()
