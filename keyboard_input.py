
from gpiozero import LED
from time import sleep
import numpy as np
import os
import sys,tty,termios
import RPi.GPIO as GPIO

class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get(led_matrix,prev_pos):
    inkey = _Getch()
    while(1):
        k=inkey()
        if k!='':
            break
    if k=='\x1b[A':
            print("up")
            new_pos = prev_pos + np.array([-1,0])
    elif k=='\x1b[B':
            print ("down")
            new_pos = prev_pos + np.array([1,0])
    elif k=='\x1b[C':
            print ("right")
            new_pos = prev_pos + np.array([0,1])
    elif k=='\x1b[D':
            print ("left")
            new_pos = prev_pos + np.array([0,-1])
    #elif k=='\033':
            #print("ESC")
    else:
            print ("not an arrow key!")
            sys.exit()
    
    led_matrix[new_pos[0],new_pos[1]] = 1
    led_matrix[prev_pos[0],prev_pos[1]] = 0
    clear()
    print(led_matrix)
    return new_pos

clear = lambda: os.system('clear')

leds = [LED(26),LED(19),LED(13),LED(6),LED(5)]
w, h = 16, 16
led_matrix = np.zeros((w,h))

new_position = np.array([0,0])
#while True:
    
    #old_position = new_position
    #print("old position: " + str(old_position))
    #new_position = get(led_matrix,old_position)
    #print("new position: " + str(new_position))

def turn_on_LEDs(leds):
    leds[0].on()
    leds[1].on()
    leds[2].on()
    leds[3].on()   


def turn_off_LEDs(leds):
    leds[0].off()
    leds[1].off()
    leds[2].off()
    leds[3].off()   

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

while True:
    #GPIO.output(PINS[4], False)
    #GPIO.output(PINS[0], True)
    #GPIO.output(PINS[1], True)
    #GPIO.output(PINS[2], True)
    #GPIO.output(PINS[3], True)
    #GPIO.output(PINS[4], True)
    #sleep(0.5)
    #GPIO.output(PINS[4], False)
    #GPIO.output(PINS[0], True)
    #GPIO.output(PINS[1], True)
    #GPIO.output(PINS[2], True)
    #GPIO.output(PINS[3], False)
    #GPIO.output(PINS[4], True)
    #sleep(0.5)
    new_pattern([0,0,0,0], PINS)
    
    new_pattern([0,0,0,1], PINS)
    
    #for i in range(255):
    #    new_pattern([0,0,0,1],PINS)
       
#val = 1
#row = 0
#while True:
#    try:
#        if keyboard.is_pressed('q'):
#            print("q pressed")
#            break
#    except:
#        break
#    
#        #clear()
#        #print(led_matrix)
#        #led_matrix[2,2] = 1
#        #sleep(0.5) 


