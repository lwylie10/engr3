import time
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import servo

angle=90 #assigning a starting value to my angle variable 

pwm = pwmio.PWMOut(board.D6, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

btn = DigitalInOut(board.D5)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

btn2 = DigitalInOut(board.D4)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN

while True:
    if  angle<180:
        if btn.value:   #if button 1 is pressed
            print(angle)    #print the angle
            angle = angle+90 #
            my_servo.angle = angle
            time.sleep(0.02)
    if angle>0:    
            if btn2.value:
               print(angle)
               angle = angle-90
               my_servo.angle = angle
               time.sleep(0.02)


            time.sleep(0.1) # sleep for debounce