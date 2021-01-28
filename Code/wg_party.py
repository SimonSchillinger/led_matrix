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


#GPIO.output(MUX_Z, GPIO.HIGH)
def set_GPIOs(enable_mux, state_S3, state_S2, state_S1, state_S0):
     #GPIO.output(MUX_Z, enable_mux)
   #sleep(0.01)
    GPIO.output(MUX_S0, state_S0)
    GPIO.output(MUX_S1, state_S1)
    GPIO.output(MUX_S2, state_S2)
    GPIO.output(MUX_S3, state_S3)
    GPIO.output(MUX_Z, GPIO.LOW)
    
def enable_row(led_id, sleep_duration):
    if led_id == 0:
        set_GPIOs(1,0,0,0,0)
    if led_id == 1:
        set_GPIOs(1,0,0,0,1)
    if led_id == 2:
        set_GPIOs(1,0,0,1,0)
    if led_id == 3:
        set_GPIOs(1,0,0,1,1)
    if led_id == 4:
        set_GPIOs(1,0,1,0,0)
    if led_id == 5:
        set_GPIOs(1,0,1,0,1)
    if led_id == 6:
        set_GPIOs(1,0,1,1,0)
    if led_id == 7:
        set_GPIOs(1,0,1,1,1)
    if led_id == 8:
        set_GPIOs(1,1,0,0,0)
    if led_id == 9:
        set_GPIOs(1,1,0,0,1)
    if led_id == 10:
        set_GPIOs(1,1,0,1,0)
    if led_id == 11:
        set_GPIOs(1,1,0,1,1)
    if led_id == 12:
        set_GPIOs(1,1,1,0,0)
    if led_id == 13:
        set_GPIOs(1,1,1,0,1)
    if led_id == 14:
        set_GPIOs(1,1,1,1,0)
    if led_id == 15:
        set_GPIOs(1,1,1,1,1)
    sleep(sleep_duration)
    #set_GPIOs(0,0,0,0,0)
    #sleep(3)
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





#define LETTERS/NUMBERS
top_top = np.transpose(np.array([
 [0,0,0,0, 0, 1,1,1,1,1,1, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],]))
top_left =  np.transpose(np.array([
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 1, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 1, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 1, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 1, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 1, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 1, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],]))

top_right = np.transpose(np.array([
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 1, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 1, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 1, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 1, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 1, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 1, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],]))

middle =  np.transpose(np.array([
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 1,1,1,1,1,1, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],]))

bottom_left =  np.transpose(np.array([
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 1, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 1, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 1, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 1, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 1, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 1, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],]))

bottom_right =  np.transpose(np.array([
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 1, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 1, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 1, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 1, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 1, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 1, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],]))


bottom_bottom =  np.transpose(np.array([
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 1,1,1,1,1,1, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],]))


zero_array =  np.transpose(np.array([
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],
 [0,0,0,0, 0, 0,0,0,0,0,0, 0, 0,0,0,0],]))


# DEFINE CHARACTERS
character_2_list = [top_top,top_left, middle, bottom_right, bottom_bottom]
character_0_list = [top_top,top_left,top_right,bottom_left,bottom_right,bottom_bottom]
character_1_list = [top_right, bottom_right]

character_2 = zero_array
for array in character_2_list:
    character_2 = character_2 + array

character_0 = zero_array
for array in character_0_list:
    character_0 = character_0 + array

character_1 = zero_array
for array in character_1_list:
    character_1 = character_1 + array

#ANIMATIONS

def anim_iterate_through_all_leds(sleep_duration,repeat_num):
    for repeat_iter in np.arange(repeat_num):
        if repeat_iter%2 == 1:
            start = 2
        else:
            start = 0
        for row_idx in np.arange(start,16):
            row_array = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0] 
            for column_idx in np.arange(len(row_array)):
                if row_idx%2 == 0:
                    row_array[column_idx] = 1
                else:
                    row_array[len(row_array)-column_idx-1] = 1
                set_row(row_array)
                if repeat_iter%2 == 0:
                    enable_row(row_idx, sleep_duration)
                else:
                    enable_row(16-row_idx,sleep_duration)

def anim_all_leds_from_left_to_right(sleep_duration, direction, repeat_num):
    row_array = [1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1]
    set_row(row_array)
    for repeat_iter in np.arange(repeat_num):
        if direction == 'backwards':
            for row_idx in np.arange(16):
                enable_row(16-row_idx, sleep_duration)
        if direction == 'forwards':
            for row_idx in np.arange(16):
                enable_row(row_idx, sleep_duration)
        if direction == 'for_and_backwards':
            if repeat_iter == 1:
                for row_idx in np.arange(16):
                    enable_row(row_idx, sleep_duration)
            else:
                for row_idx in np.arange(16):    
                    enable_row(row_idx, sleep_duration)
            for row_idx in np.arange(2,16):
                enable_row(16-row_idx, sleep_duration)


def anim_triangle_leds_from_left_to_right(sleep_duration, direction, repeat_num):
    for repeat_iter in np.arange(repeat_num):
        row_array = [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0]
        set_row(row_array)
        if direction == 'backwards':
            for row_idx in np.arange(16):
                row_array[row_idx] = ~row_array[row_idx]
                set_row(row_array)
                enable_row(16-row_idx, sleep_duration)
        if direction == 'forwards':
            for row_idx in np.arange(16):
                row_array[row_idx] = ~row_array[row_idx]
                set_row(row_array)
                enable_row(row_idx, sleep_duration)
        if direction == 'for_and_backwards':
            if repeat_iter == 1:
                for row_idx in np.arange(16):
                    row_array[row_idx] = ~row_array[row_idx] 
                    set_row(row_array)
                    enable_row(row_idx, sleep_duration)
            else:
                for row_idx in np.arange(16):    
                    row_array[row_idx] = ~row_array[row_idx]
                    set_row(row_array)
                    enable_row(row_idx, sleep_duration)
            for row_idx in np.arange(2,16):
                row_array[row_idx-2] = ~row_array[row_idx-2]
                set_row(row_array)
                enable_row(16-row_idx, sleep_duration)



def anim_2021(sleep_duration,show_num,counter):
    for couunter_iter in np.arange(counter):
    
        step_further = 0
        for row_idx in np.arange(4,12):
            idx = row_idx            
            enable_row(row_idx,sleep_duration)
            if show_num == '2':
                set_row(character_2[idx])
            if show_num == '0':
                set_row(character_0[idx])
            if show_num == '1':
                set_row(character_1[idx])
    GPIO.output(MUX_Z, GPIO.HIGH) 
    
def anim_2021_complete():
    anim_2021(0,'2',1000)
    sleep(0.5)
    anim_2021(0,'0',1000)
    sleep(0.5)
    anim_2021(0,'2',1000)
    sleep(0.5)
    set_row([1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1])
    enable_row(8,1)
    
repeat_num = 2
while True:
    for speed in [0.15, 0.125, 0.1, 0.125, 0.15]:
        speed = speed/3
        anim_iterate_through_all_leds(speed/10, repeat_num)    
        anim_triangle_leds_from_left_to_right(speed, 'forwards', repeat_num)
        anim_triangle_leds_from_left_to_right(speed, 'backwards', repeat_num)
        anim_triangle_leds_from_left_to_right(speed, 'for_and_backwards', repeat_num)
        
        anim_all_leds_from_left_to_right(speed, 'forwards', repeat_num)
        anim_all_leds_from_left_to_right(speed, 'backwards', repeat_num)
        anim_all_leds_from_left_to_right(speed, 'for_and_backwards', repeat_num)
        anim_2021_complete()

       
