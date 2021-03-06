import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time
import sys

'''

Object used to interface clients with ADC measurement initiations. Object
is agnostic to which cell it interfaces with.

'''
class ADCControlFactory(object):
    '''
    Instantiates an identifiable ADCControlFactory instance

    val: integer to identify the instantiated class
    return: instance of ADCControlFactory
    '''
    def __init__(self,val):
        self.val = val
        self.previousValue = 0

    '''
    Setup the Pi to interpret ADC readings from selected solar cell over
    a fixed 10 second interval

    return: average float from 20 measurements
    '''
    def gatherADCData(self):
        # Software SPI configuration:
        CLK  = 18
        MISO = 23
        MOSI = 24
        CS   = 25
        mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
        ADC_CHANNEL = 1

        # Read all the ADC channel values in a list.
        total = 0
        print("Interpreting data...")
        initialMeasurement = True
        initialDelay = 10021
        for measurementNumber in range(initialDelay):
            # Allows for measurements to stabilize using count
            if(measurementNumber > 10000):
                values = [0]*1
                values[0] = (mcp.read_adc(ADC_CHANNEL) * (3.3/1023))/1000
                print(values[0])

                if(initialMeasurement):
                    self.previousValue = values[0]

                try:
                    if(self.isDisconnected(self.previousValue, values[0])):
                        raise ValueError('ERROR: TEST HARDWARE DISCONNECTED')
                    if(self.isCloudCovered(self.previousValue, values[0])):
                        raise ValueError('SUSPENDED TEST: CLOUD COVERAGE DURING TEST')
                except (ValueError) as error:
                    print(repr(error))
                    raise error

                total = total + values[0]
                self.previousValue = values[0]
                initialMeasurement = False

                time.sleep(0.5)

        return total/20.0

    def isDisconnected(self, oldValue, newValue):
        if(newValue == 0):
            return True
        return False

    def isCloudCovered(self, oldValue, newValue):
        if(oldValue == newValue):
            return False
        if((abs(oldValue - newValue)/oldValue)*100 > 30):
            return True
        return False
