# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Main program loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*1
    values[0] = mcp.read_adc(0) * (3.3/1023)
    # Print the ADC values.
    print(str(values[0]) + ' V')
    # Pause for half a second.
    time.sleep(0.5)
