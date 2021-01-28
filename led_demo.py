
from gpiozero import LED
from time import sleep
import numpy as np
import os
import sys,tty,termios
import RPi.GPIO as GPIO


def new_pattern(pattern,PINS):
    for i in range(4):
        if pattern[i] == 0:
            GPIO.output(PINS[i], False)
        else:
            GPIO.output(PINS[i], True)
    GPIO.output(PINS[4], True)
    sleep(0.5)
    GPIO.output(PINS[4], False)


PINS = [26,19,13,6,5]

GPIO.setmode(GPIO.BCM)
GPIO.setup(PINS[0], GPIO.OUT)
GPIO.setup(PINS[1], GPIO.OUT)
GPIO.setup(PINS[2], GPIO.OUT)
GPIO.setup(PINS[3], GPIO.OUT)
GPIO.setup(PINS[4], GPIO.OUT)

GPIO.output(PINS[0], GPIO.HIGH)
GPIO.output(PINS[1], GPIO.HIGH)
GPIO.output(PINS[2], True)
GPIO.output(PINS[3], True)
GPIO.output(PINS[4], True)
sleep(10)
GPIO.cleanup()
#    sleep(0.001)
#    GPIO.output(PINS[0],False)
#    for i in range(15):
#        GPIO.output(PINS[1],True)
#        sleep(0.001)
#        GPIO.output(PINS[1],False)

