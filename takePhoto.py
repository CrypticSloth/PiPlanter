#Take a photo
#NOTE: this can only be done on raspian operating system
# to make use of the raspistill command

import os
import time

count = 0
while count <= 0:
	os.system('raspistill -o image{}.jpg'.format(count))
	print('Taking photo {}'.format(count))
	count +=  1
	time.sleep(1)

print('All Done')

