from gpiozero import LED
from time import sleep
import RPi.GPIO as GPIO
import numpy as np

GPIO.setmode(GPIO.BCM)

#define PINS
#MULTIPLEXER
MUX_Z  = 27
MUX_S3 = 22
MUX_S2 = 10
MUX_S1 = 9
MUX_S0 = 11
#HIGH-SIDE(HS)  SWITCH
HS_0 = 17
HS_1 = 4
HS_2 = 3
HS_3 = 2
HS_4 = 14
HS_5 = 15
HS_6 = 18
HS_7 = 23
HS_8 = 24
HS_9 = 25
HS_10 = 8
HS_11 = 7
HS_12 = 26
HS_13 = 19
HS_14 = 13
HS_15 = 6

#setting up low side switch PINS
GPIO.setup(MUX_Z,GPIO.OUT)
GPIO.setup(MUX_S3,GPIO.OUT)
GPIO.setup(MUX_S2,GPIO.OUT)
GPIO.setup(MUX_S1,GPIO.OUT)
GPIO.setup(MUX_S0,GPIO.OUT)

#setting up high side switch PINS
GPIO.setup(HS_0, GPIO.OUT)
GPIO.setup(HS_1, GPIO.OUT)
GPIO.setup(HS_2, GPIO.OUT)
GPIO.setup(HS_3, GPIO.OUT)
GPIO.setup(HS_4, GPIO.OUT)
GPIO.setup(HS_5, GPIO.OUT)
GPIO.setup(HS_6, GPIO.OUT)
GPIO.setup(HS_7, GPIO.OUT)
GPIO.setup(HS_8, GPIO.OUT)
GPIO.setup(HS_9, GPIO.OUT)
GPIO.setup(HS_10, GPIO.OUT)
GPIO.setup(HS_11, GPIO.OUT)
GPIO.setup(HS_12, GPIO.OUT)
GPIO.setup(HS_13, GPIO.OUT)
GPIO.setup(HS_14, GPIO.OUT)
GPIO.setup(HS_15, GPIO.OUT)


def set_GPIOs(state_S3, state_S2, state_S1, state_S0):
    GPIO.output(MUX_Z, GPIO.LOW)
    GPIO.output(MUX_S0, state_S0)
    GPIO.output(MUX_S1, state_S1)
    GPIO.output(MUX_S2, state_S2)
    GPIO.output(MUX_S3, state_S3)
    GPIO.output(MUX_Z, GPIO.HIGH)
    
def enable_row(led_id):
    if led_id == 0:
        set_GPIOs(0,0,0,0)
    if led_id == 1:
        set_GPIOs(0,0,0,1)
    if led_id == 2:
        set_GPIOs(0,0,1,0)
    if led_id == 3:
        set_GPIOs(0,0,1,1)
    if led_id == 4:
        set_GPIOs(0,1,0,0)
    if led_id == 5:
        set_GPIOs(0,1,0,1)
    if led_id == 6:
        set_GPIOs(0,1,1,0)
    if led_id == 7:
        set_GPIOs(0,1,1,1)
    if led_id == 8:
        set_GPIOs(1,0,0,0)
    if led_id == 9:
        set_GPIOs(1,0,0,1)
    if led_id == 10:
        set_GPIOs(1,0,1,0)
    if led_id == 11:
        set_GPIOs(1,0,1,1)
    if led_id == 12:
        set_GPIOs(1,1,0,0)
    if led_id == 13:
        set_GPIOs(1,1,0,1)
    if led_id == 14:
        set_GPIOs(1,1,1,0)
    if led_id == 15:
        set_GPIOs(1,1,1,1)
    sleep(0.01)

def set_row(row_array):
    GPIO.output(HS_0,row_array[0])
    GPIO.output(HS_1,row_array[1])
    GPIO.output(HS_2,row_array[2])
    GPIO.output(HS_3,row_array[3])
    GPIO.output(HS_4,row_array[4])
    GPIO.output(HS_5,row_array[5])
    GPIO.output(HS_6,row_array[6])
    GPIO.output(HS_7,row_array[7])
    GPIO.output(HS_8,row_array[8])
    GPIO.output(HS_9,row_array[9])
    GPIO.output(HS_10,row_array[10])
    GPIO.output(HS_11,row_array[11])
    GPIO.output(HS_12,row_array[12])
    GPIO.output(HS_13,row_array[13])
    GPIO.output(HS_14,row_array[14])
    GPIO.output(HS_15,row_array[15])

row_array = [1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1]
set_row(row_array)

#HALLO_array =[[0,0,0,0, 0,0,1,1, 1,1,1,0, 0,0,0,0],
# [0,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0],
# [0,0,0,0, 0,0,1,1, 1,1,1,0, 0,0,0,0],
# [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
# [0,0,0,0, 0,0,1,1, 1,1,1,0, 0,0,0,0],
# [0,0,0,0, 0,0,0,0, 1,0,1,0, 0,0,0,0],
# [0,0,0,0, 0,0,1,1, 1,1,1,0, 0,0,0,0],
# [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
# [0,0,0,0, 0,0,1,1, 1,1,1,0, 0,0,0,0],
# [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
# [0,0,0,0, 0,0,1,1, 1,1,1,0, 0,0,0,0],
# [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
# [0,0,0,0, 0,0,1,1, 1,1,1,0, 0,0,0,0],
# [0,0,0,0, 0,0,1,0, 0,0,1,0, 0,0,0,0],
# [0,0,0,0, 0,0,1,1, 1,1,1,0, 0,0,0,0],
# [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
#]

HALLO_array =[
 [0,0,0,0, 0,0,1,1, 1,1,1,0, 0,0,0,0],
 [0,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0],
 [0,0,0,0, 0,0,1,1, 1,1,1,0, 0,0,0,0],
 [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
 [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
 [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
 [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
 [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
 [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
 [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
 [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
 [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
 [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
 [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
 [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
 [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0],
 ]


step_further = 0
counter = 0
while True:
    for row_idx in np.arange(16):
        row_array = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0] 
        for column_idx in np.arange(len(row_array)):
            if row_idx%2 == 0:
                row_array[column_idx] = 1
            else:
                row_array[len(row_array)-column_idx-1] = 1
            set_row(row_array)
            enable_row(row_idx)
    #for row_idx in np.arange(16):
    #    if counter < 1000:
    #        idx = row_idx + step_further
    #        set_row(HALLO_array[idx%16])
    #        enable_row(row_idx)
    #        counter = counter + 1
    #    else:
    #        step_further = step_further + 1
    #        counter = 0
    #enable_row(0)
    #enable_row(1)   
    #enable_row(2) 
    #enable_row(3)
    #enable_row(4)
    #enable_row(5)
    #enable_row(6)
    #enable_row(7)
    #enable_row(8)
    #enable_row(9)
    #enable_row(10)
    #enable_row(11)
    #enable_row(12)
    #enable_row(13)
    #enable_row(14)
    #enable_row(15)
    
