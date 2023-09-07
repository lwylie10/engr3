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
GREEN = (0, 255, 0)

while True:
    try:
        print(sonar.distance)
        if sonar.distance <= 5:
            neopixel.fill(255, 0 ,0)       
            print("something happy")

    except:
        print("gfdsijojoidsgjoisdgroij")
        time.sleep(0.1)
    