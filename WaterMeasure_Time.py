#record water sensor every 15 min

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

#how often to record water sensor measurements (in seconds)
time_to_wait = 1
   
print("Records the moisture sensor measurement every {0} minutes").format(time_to_wait / 60)
print("Press ^C to end the program")
print("\n")
      
while True:
    print(str(time.ctime()) + ": " + str(mcp.read_adc(5))) 
    time.sleep(time_to_wait)
