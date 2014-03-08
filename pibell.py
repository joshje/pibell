#!/usr/bin/env python
from twython import Twython
import RPi.GPIO as GPIO
import time
import os
import sys
import random
import config

buttonPin = 17
haltPin = 4
ledPin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)
GPIO.setup(haltPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)
twitter = Twython(config.api_key,config.api_secret,config.access_key,config.access_secret)

messages = [
    'hey, someone just rang your doorbell',
    'ding dong, ding dong',
    'knock knock, who\'s there?',
    'yo, someone\'s at the door',
    'yo, the bell just went',
    'are you going to get that or shall I?'
]

def sendStatusMessage():
    status = ''
    if (config.mentions): status += ' '.join(config.mentions) + ' '
    status += random.choice(messages)
    if (config.debug): print status
    else: twitter.update_status(status=status)

wasPressed = GPIO.input(buttonPin)

try:
    while True:
	if (GPIO.input(haltPin)):
            print 'shutting down'
            GPIO.cleanup()
            if not config.debug: os.system('sudo halt')
            sys.exit()
        isPressed = GPIO.input(buttonPin)
        if ((not wasPressed) and isPressed):
            sendStatusMessage()
	    GPIO.output(ledPin, True)
	    time.sleep(5)
	    GPIO.output(ledPin, False)
        wasPressed = isPressed
        time.sleep(0.05)
except KeyboardInterrupt:
    GPIO.cleanup()
