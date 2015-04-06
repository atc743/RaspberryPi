#!/usr/bin/env python
import sys
from twython import Twython
from time import sleep
import RPi.GPIO as GPIO

CONSUMER_KEY = '*******KEY*******'
CONSUMER_SECRET = '*******SECRET*******'
ACCESS_KEY = '*******KEY*******'
ACCESS_SECRET = '*******SECRET*******'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)


print('running')
time = 0

while 1:
	sleep(1)
	if GPIO.input(11):
		(time = time + 1)
		print('button is pressed for '+str(time)+' seconds')
	elif time != 0:
			if time > 10 and time < 60:
				printThrone = 'The King has been sitting on the throne for '+str(time)+' seconds.'
				print(printThrone)
		                twitter.update_status(status=printThrone)
               			time = 0
			elif time >= 60 and time < 120:
				printThrone = 'The King has been sitting on the throne for 1  minute and '+str(time%60)+' seconds.'
				print(printThrone)
		                twitter.update_status(status=printThrone)
        		        time = 0
			elif time >= 120:
				printThrone = 'The King has been sitting on the throne for '+str(time/60)+' minutes and '+str(time%60)+' seconds.' 
				print(printThrone)
				twitter.update_status(status=printThrone)
				time = 0
