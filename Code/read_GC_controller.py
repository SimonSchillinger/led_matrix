from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    i = GPIO.input(5)
    print("Hello" + str(i))
    
