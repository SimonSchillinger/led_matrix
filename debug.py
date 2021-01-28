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


def set_GPIOs(enable_mux, state_S3, state_S2, state_S1, state_S0):
    GPIO.output(MUX_Z, enable_mux)
    GPIO.output(MUX_S0, state_S0)
    GPIO.output(MUX_S1, state_S1)
    GPIO.output(MUX_S2, state_S2)
    GPIO.output(MUX_S3, state_S3)
    GPIO.output(MUX_Z, GPIO.HIGH)
    
def enable_row(led_id, sleep_duration):
    if led_id == 0:
        set_GPIOs(0,0,0,0,0)
    if led_id == 1:
        set_GPIOs(0,0,0,0,1)
    if led_id == 2:
        set_GPIOs(0,0,0,1,0)
    if led_id == 3:
        set_GPIOs(0,0,0,1,1)
    if led_id == 4:
        set_GPIOs(0,0,1,0,0)
    if led_id == 5:
        set_GPIOs(0,0,1,0,1)
    if led_id == 6:
        set_GPIOs(0,0,1,1,0)
    if led_id == 7:
        set_GPIOs(0,0,1,1,1)
    if led_id == 8:
        set_GPIOs(0,1,0,0,0)
    if led_id == 9:
        set_GPIOs(0,1,0,0,1)
    if led_id == 10:
        set_GPIOs(0,1,0,1,0)
    if led_id == 11:
        set_GPIOs(0,1,0,1,1)
    if led_id == 12:
        set_GPIOs(0,1,1,0,0)
    if led_id == 13:
        set_GPIOs(0,1,1,0,1)
    if led_id == 14:
        set_GPIOs(0,1,1,1,0)
    if led_id == 15:
        set_GPIOs(0,1,1,1,1)
    sleep(sleep_duration)
    set_GPIOs(1,0,0,0,0)
    sleep(3)
def set_row(row_array):
    GPIO.output(HS_0,int(row_array[0]))
    GPIO.output(HS_1,int(row_array[1]))
    GPIO.output(HS_2,int(row_array[2]))
    GPIO.output(HS_3,int(row_array[3]))
    GPIO.output(HS_4,int(row_array[4]))
    GPIO.output(HS_5,int(row_array[5]))
    GPIO.output(HS_6,int(row_array[6]))
    GPIO.output(HS_7,int(row_array[7]))
    GPIO.output(HS_8,int(row_array[8]))
    GPIO.output(HS_9,int(row_array[9]))
    GPIO.output(HS_10,int(row_array[10]))
    GPIO.output(HS_11,int(row_array[11]))
    GPIO.output(HS_12,int(row_array[12]))
    GPIO.output(HS_13,int(row_array[13]))
    GPIO.output(HS_14,int(row_array[14]))
    GPIO.output(HS_15,int(row_array[15]))


GPIO.output(MUX_Z, 

while True:
    sleep(1)
