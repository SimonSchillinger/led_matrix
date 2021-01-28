import numpy as np
import matplotlib as plt
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.OUT)

pi_pwm = GPIO.PWM(12,10000)
pi_pwm.start(0)
pi_pwm.ChangeDutyCycle(50)
previous_input = 0

mynum = 0
def my_callback(channel):
    global mynum
    mynum = mynum + 1
    if mynum == 10000:
        print(mynum)
        mynum = 0

GPIO.add_event_detect(7, GPIO.RISING, callback = my_callback)

sleep(10)
        
