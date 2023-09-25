import time 
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import motor
import analogio
spinny = pwmio.PWMOut(board.D6, duty_cycle=65535,frequency = 5000 )# wire in pin 5 with pwm
speed = analogio.AnalogIn(board.A1)#the potentiometer's pin and defining it to "speed"
while True:
    sdfg = speed.value#this is reading the value of the potentiometer and defining it
    spinny.duty_cycle = sdfg#this is the pwm output and the speed of the motor based off of the potentiometer