import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D8, echo_pin=board.D7)
import neopixel
from rainbowio import colorwheel
import simpleio

NUMPIXELS = 1
SPEED = 0.05
BRIGHTNESS = 0.1
PIN = board.NEOPIXEL
red=0
blue=0
green=0

cm = 0
pixel = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=0.2, auto_write=False)
while True:
    try:
        cm = sonar.distance  
        if cm >= 0 and cm <=20:
            red = simpleio.map_range(cm, 5, 20, 255, 0)
            blue = simpleio.map_range(cm, 5, 20, 0, 255)
            green = 0
            print(cm)
            pixel.fill((red, green, blue)) 
            pixel.show()      
            time.sleep(0.1)
        elif cm >= 20 and cm <=35: 
            red = 0
            blue = simpleio.map_range(cm, 20, 35, 255, 0)
            green = simpleio.map_range(cm, 20, 35, 0, 255)
            print(cm)
            pixel.fill((red, green, blue))
            pixel.show()
            time.sleep(0.1)
        elif cm > 35 and cm < 120:
            green = 255
            pixel.fill(green)
            red = 0
            blue = 0
            pixel.show
            print (cm)
            time.sleep(0.1)
    except:
        print("i crashed")
        time.sleep(0.1)