import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time
from threading import Thread

class ADCThread(Thread):

    '''
    This instantiates the Thread to interpret the ADC readings into Terminal
    '''
    def __init__(self,val):

        Thread.__init__(self)
        self.val = val

    '''
    This runs the Thread to setup the Pi to interpret ADC readings
    '''
    def run(self):

        # Software SPI configuration:
        CLK  = 18
        MISO = 23
        MOSI = 24
        CS   = 25
        mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

        # Read all the ADC channel values in a list.
        for i in range(20):
            values = [0]*1
            values[0] = (mcp.read_adc(0) * (3.3/1023))/1000
            # Print the ADC values.
            print(str(values[0]) + ' A')
            # Pause for half a second.
            time.sleep(0.5)
