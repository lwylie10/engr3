import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D8, echo_pin=board.D7)
import neopixel
from rainbowio import colorwheel

NUMPIXELS = 1
SPEED = 0.05
BRIGHTNESS = 0.1
PIN = board.NEOPIXEL
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
cm = 0
pixel = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=0.3, auto_write=False)
while True:
    try:
        cm = sonar.distance  
        print(cm)
        if cm <= 5:
            pixel.fill(RED) 
            pixel.show()      
            time.sleep(0.1)
        elif cm <= 20: 
            pixel.fill(GREEN)
            pixel.show()
            time.sleep(0.1)
        else:
            pixel.fill(BLUE)
            pixel.show
            time.sleep(0.1)
    except:
        print("gfdsijojoidsgjoisdgroij")
        time.sleep(0.1)