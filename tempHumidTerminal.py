#DHT humidity and temp sensor code

import sys
import Adafruit_DHT

while True:
	humidity, temp_C  = Adafruit_DHT.read_retry(11,4)
	temp_F = temp_C * 9/5 + 32
	print('Temp: C = {0:0.1f} F = {1:0.1f} Humidity: {2:0.1f}%'.format(temp_C, temp_F, humidity)) 

