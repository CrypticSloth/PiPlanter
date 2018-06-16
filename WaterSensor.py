#Water Sensor for PiPlanter
#Plugged into GPIO 21

from time import sleep
import mcp3008

while True:
  m = mcp3008.readadc(21)
  print "Moisture level: %d ".format(m)
  sleep(.5)

