# Using crontab to run every 15 minutes:
# contab -e
# 0,15,30,45 * * * * python WaterSensorLog.py

# Water sensor log
import numpy as np
import pandas as pd
import datetime
from time import sleep
import Adafruit_MCP3008
import Adafruit_DHT

# Setup the mcp3008
CLK = 18
MISO = 23
MOSI = 24
CS = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK,cs=CS,miso=MISO,mosi=MOSI)

# GATHER THE DATA
moisture = mcp.read_adc(5)
humidity, temp_C = Adafruit_DHT.read_retry(11,4)
temp_F = temp_C * 9/5 + 32

# Take the mean of the past x (seconds) moisture sensor readings 
# for precision since the sensor produces highly variable readings
# every second. 

x = 10
readings = []
for i in range(x):
    readings.append(moisture)
    sleep(1)

moisture_avg = np.mean(readings)
moisture_med = np.median(readings)

# STORING THE DATA 
csv_file_name = "/home/pi/PiPlanter/LoggingPlantData.csv"

date = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())

# Reading the Data Frame in append mode ('a')
df = open(csv_file_name,'a')


# APPEND NEW DATA TO DATA FRAME

df.write(date)
df.write(', ')
df.write(str(moisture_med))
df.write(', ')
df.write(str(humidity))
df.write(', ')
df.write(str(temp_F))
df.write('\n')
df.close()
