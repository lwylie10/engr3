# CircuitPython
 [ directory of all students!](https://github.com/chssigma/Class_Accounts)
## Table of Contents
### Arduino
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [Circuit Python Distance Sensor](#Circuit_Python_Distance_Sensor)
* [Motor Control](#Motor_Control)
* [Photointeruppter](#Photointeruppter)
### Onshape
* [NextAssignmentGoesHere](#NextAssignment)
---
## Hello_CircuitPython🌾
### Description & Code Snippets
The assignment was to use code to get an RGB LED glowing in a rainbow pattern and make it fade in and out between colors really smoothly.

```python

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)\
def rainbow_cycle(wait):
    for color in range(255):
        for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
            pixel_index = (pixel * 256 // len(pixels)) + color * 5
            pixels[pixel] = colorwheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)
while True:
    rainbow_cycle(SPEED)
```

[C:\Users\abuckne38\Documents\engr3\hello.py
](https://github.com/addddddy/engr3/blob/main/hello.py)

### Evidence

![ezgif com-video-to-gif](https://github.com/addddddy/engr3/assets/143544940/8e3104e2-fc72-45ad-a922-281586c123d8)

Photo creds to the WONDERFUL Addy Buckner 😍
[Addy Buckner's Github](https://github.com/addddddy)

### Wiring
We literally had no wiring. The neopixel is directly attached to the board, so all we had to do was plug in the board
<img src="https://cdn-learn.adafruit.com/assets/assets/000/041/507/original/microcontrollers_3505_iso_ORIG.jpg">
Image credit goes to [Lady Ada](https://learn.adafruit.com/adafruit-metro-m0-express)

### Reflection
I started with googling for the code and i found code called some along the lines of "neopixel rainbow test". All I had to do after that was rewrite a couple of the lines to fix some of the bugs my board had with it and then it worked fine. It was a fun assignment and using the pixel index was cool and I was able to change how fast the color changed between 0 and 256.

## CircuitPython_Servo🌹

### Description & Code Snippets

The assignment is to get a 180° micro servo to slowly sweep back and forth between 0 and 180°.   

```python
import time
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import servo

angle=90 #assigning a starting value to my angle variable 

pwm = pwmio.PWMOut(board.D6, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

btn = DigitalInOut(board.D5)#wire in pin D5
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

btn2 = DigitalInOut(board.D4)#wire in pin D4
btn2.direction = Direction.INPUT#button is input
btn2.pull = Pull.DOWN#if nothings pressing it it = 0(thats why i dont need a resistor)

while True:
    if  angle<180:
        if btn.value:   #if button 1 is pressed
            print(angle)    #print the angle
            angle = angle+90 #add 90 degrees to the code
            my_servo.angle = angle
            time.sleep(0.02)
    if angle>0:    
            if btn2.value: #same thing as above
               print(angle)
               angle = angle-90
               my_servo.angle = angle
               time.sleep(0.02)


            time.sleep(0.1) # sleep for debounce

```

(https://github.com/lwylie10/engr3/blob/main/servo.py)


### Evidence

![ezgif com-optimize](https://github.com/addddddy/engr3/assets/143544940/561c9908-fda6-4a8d-a112-b2ad3f70374c)

This beautiful GIF was finely produced by Addy Buckner
[Addy's Github](https://github.com/addddddy)

### Wiring
![image](https://github.com/lwylie10/engr3/assets/143544940/8cbd44c2-ff50-4534-8e8f-f62179d86f09)


### Reflection
This assignment was definitly harder then the last one because I had to spend a long time on tweaking the servo values and the different commands to make it less buggy. I had the most trouble with making sure that wherever the servo arm was, when i clicked the button it would move 90 degrees in the direction i wanted it to. it challenged me to think about the way i was coding and what values i had to use to make it less buggy.


## Circuit_Python_Distance_Sensor🌷
### Description & Code Snippets
Use the HC-SR04 to measure the distance to an object and print that out to your serial monitor or LCD in cm.
Next, you will get the neopixel to turn red when your object is less than 5cm, and green when its 35cm. For the final version of this code, you'll smoothly shift the color of the onboard neopixel, corresponding to the distance, according to the graphic below.
(Neopixel should stay red when below 5cm and green when above 35cm)
  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D8, echo_pin=board.D7)
import neopixel
from rainbowio import colorwheel
import simpleio

NUMPIXELS = 1#using the neopixel
SPEED = 0.05
BRIGHTNESS = 0.1#the brightness of the pixel
PIN = board.NEOPIXEL
red=0
blue=0
green=0

cm = 0
pixel = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=0.2, auto_write=False)
while True:
    try: #try this code
        cm = sonar.distance  
        if cm >= 0 and cm <=20:#between the values of 0 and 20 cm
            red = simpleio.map_range(cm, 5, 20, 255, 0)#slowly shift the red values from full(255) to 0
            blue = simpleio.map_range(cm, 5, 20, 0, 255)#start blue at zero and increase the blueness of the pixel untill 255 at 20cm
            green = 0#not doing anything yet
            print(cm)
            pixel.fill((red, green, blue)) #fill the pixel in with RGB
            pixel.show()      
            time.sleep(0.1)
        elif cm >= 20 and cm <=35: #same thing with the last if statement except its with 20 to 35 cm
            red = 0#not in the range of colors
            blue = simpleio.map_range(cm, 20, 35, 255, 0)#blue starts at full at 20 cm and slowly moves to zero at 35cm
            green = simpleio.map_range(cm, 20, 35, 0, 255)#green starts at zero and the pixel will turn to full green(255) at 35cm
            print(cm)
            pixel.fill((red, green, blue))
            pixel.show()
            time.sleep(0.1)
        elif cm > 35 and cm < 120: #when the distance sensor reads 35 to 120
            green = 255
            pixel.fill(green) #make the pixel green
            red = 0
            blue = 0
            pixel.show
            print (cm)
            time.sleep(0.1)
    except:# if none of this code applies/works print this statement instead of stopping completely
        print("i crashed")
        time.sleep(0.1)
```

**(https://github.com/lwylie10/engr3/blob/main/ultrasensorrange.py)**  

### Evidence


https://github.com/addddddy/engr3/assets/143544940/452524df-8441-4da1-8679-6953b6bb34ee


### Wiring
![image](https://github.com/lwylie10/engr3/assets/143749987/1cccb58a-4a70-44e3-95d9-08bcda33996e)

### Reflection
The assignment took me a week because at first i spent a really long time trying to figure out my buggy board issues but once i figured out what the problem was, i could work on my code. i first did the simple part which was making an if statement to change the color of the neopixel based on the values that the distance sensor was printing out. then i had to add the library. once i looked up the commands and all of the code it was easy to paste in the rest of the code to make it work. it was fun to watch the colors change. <- i wrote this :)

## Motor_Control🪻
### Description & Code Snippets
 
I have to wire up a 6v battery pack to a circuit with a motor and then write the code to make the motor speed up and slow down, based on input from a potentiometer.
```python
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

```

[link to code](https://github.com/addddddy/engr3/blob/main/asdfgh.py)
### Evidence
https://github.com/addddddy/engr3/assets/143544940/27924682-3d5d-4cbe-a117-53e67b813979
### Wiring!
![image](https://github.com/addddddy/engr3/assets/143544940/5020c688-c09c-4a59-a916-80cab3360c4b)

### Reflection
So, the assignment turned out to be way easier than I thought at first. Spent ages trying to set up this elaborate system for reading the potentiometer and controlling the motor, only to find out we just had to read the potentiometer value, send it to the board, and let the board do the heavy lifting. All we did was hook up pin 5, told the board we're using analog pin 1 for the potentiometer, and boom, the board did all the math, creating the table for different speeds based on the values.




## Photointeruppter🌻
### Description & Code Snippets
Wire up your photointerrupter and have it keep track of how many times it has been interrupted.
Your program outputs the count using a full sentence like "The number of interrupts is: ___" or "I have been interrupted ___ times."
The program outputs the sentence every 4 seconds.
Don't use sleep(), use time.monotonic().

```python
import time
import board, digitalio
newt = 0
interrupter = digitalio.DigitalInOut(board.D7)
interrupter.pull = digitalio.Pull.UP
counter = 0
interrupt = False
while True:
    if interrupter.value == 1:       
            counter = counter + 1       #count up by one if counter value = 1 
            time.sleep(0.2)
    if time.monotonic() - newt >=1:
        newt = time.monotonic()
        print ("the number of interrupts is " + str(counter))



```

[link to code](https://github.com/lwylie10/engr3/blob/main/photosensor.py)
### Evidence
![My Project](https://github.com/lwylie10/engr3/assets/143749987/ed235ea1-b424-4ad1-bfe0-54313162783f)

### Wiring

### Reflection
Doing this code basically took no time at all because when you use the provided time.monotonic() its very easy. One way to make it even better is to instead update the photointerrupter only when it
s interrupted instead of counting seconds. 



## Rotary Encoder and LCD

### Description & Code Snippets
our assignment is to use a rotary encoder, an LCD, and the on-board NeoPixel LED to create a menu-based traffic light control.
Steps:
-Create a list of strings for stop, caution, go. 
-Read the rotary encoder to cycle through the menu items and display them on the LCD.
-Make the on-board LED turn red, yellow, or green when the rotary encoder is pressed down on the corresponding menu item.

```python
import rotaryio
import time
import board
import neopixel
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3
led[0] = (255, 0, 0)
lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x27), num_rows=2, num_cols=16)
button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_state = None
menu = ["stop", "caution", "go"]
last_index = None
menu_index = 0

while True:
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        print("Button is pressed")
        button_state = None
    menu_index = enc.position
    #if last_index == None or menu_index != last_index:
        #print(menu_index)
    menu_index_lcd = menu_index % 3
    #print(menu_index_lcd)
    menu[menu_index_lcd]
    print(menu[menu_index_lcd])
    time.sleep(0.2)
    lcd.set_cursor_pos(0,0)
    lcd.print("Push For: ")
    lcd.set_cursor_pos(1,0)
    lcd.print("          ")
    lcd.set_cursor_pos(1,0)
    lcd.print(menu[menu_index_lcd])
    if menu_index_lcd == 0:
     led[0] = (255, 0, 0)
    if menu_index_lcd == 1:
     led[0] = (255, 255, 0)
    if menu_index_lcd == 2:
     led[0] = (0, 255, 0)

```

**Lastly, please end this section with a link to your code or file.**  
[link to code](https://github.com/lwylie10/engr3/blob/main/rotaryencoder.py)
### Evidence

https://github.com/lwylie10/engr3/assets/143749987/072f673a-4be0-477d-8d70-04ea0b288725

### Wiring
![Rotaryencoder](https://github.com/lwylie10/engr3/assets/143749987/48388a0f-a607-494a-b2e6-ae77b4484094)


## Reflection
This assignment was pretty difficult. Me and addy began working on it together and realized that we forgot to download all of the libraries which gave us many errors. I also had some trouble with following and tracking the spot of the rotary encoder and I had to code around that a bit. Another thing I struggled with was using the variable "menu_index_lcd" because I had to import it into the assignment so many times. Most of my errors consisted of indentation or parenthesis errors because the context was messed up or I screwed up the braces and brackets.


## Stepper Motor/Limit Switch

### Assignment Description

The goal of this assignment was to program a stepper motor to rotate until it touches the limit switch and then rotate 180 degrees in reverse when it contacts with the motor arm. This assignment was important as it teaches one to use the stepper motor which will come in handy for the robot arm project.

### Wiring Diagram
![Steppermotor](https://github.com/lwylie10/engr3/assets/143749987/1ba4b071-90d4-47b6-b201-07fdc24168c9)


### Code
```python

import asyncio
import board
import keypad
import time
import digitalio
from adafruit_motor import stepper


DELAY = 0.01  
STEPS = 100
coils = (
    digitalio.DigitalInOut(board.D9),   # A1
    digitalio.DigitalInOut(board.D10),  # A2
    digitalio.DigitalInOut(board.D11),  # B1
    digitalio.DigitalInOut(board.D12),  # B2
)


for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT
motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

async def catch_pin_transitions(pin):

    with keypad.Keys((pin,), value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event:
                if event.pressed:
                    print("Limit Switch was pressed.")
                    for step in range(STEPS):
                        motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
                        time.sleep(DELAY)
                elif event.released:
                    print("Limit Switch was released.")
            await asyncio.sleep(0)

async def run_motor():
    while(True):
        motor.onestep(style=stepper.DOUBLE)
        time.sleep(DELAY)
        await asyncio.sleep(0)

async def main():
    while(True):
        interrupt_task = asyncio.create_task(catch_pin_transitions(board.D2))
        motor_task = asyncio.create_task(run_motor())
        await asyncio.gather(interrupt_task, motor_task)

asyncio.run(main())
```

### Reflection

This assignment was pretty easy except for that I didn't realize that the assignment on canvas had already provided wiring for the H-bridge and the stepper motor and I struggled with making it for myself until benji let me know that I didn't have to do all that work. After that it wasn't that bad. I learned how to use the tool "async" a lot more with running the motor even though I had to look up a couple of times the right way to properly use it. The if statements were also a bit tricky getting all of the indentations correct and fixed up.

## IR Sensors

### Description & Code Snippets
This assignment I had to use an infrared (IR) sensor to change the color of my board’s Neopixel LED. It had to change the color red when there was an object nearby and green when there was nothing in the way

```python
# Import libraries
import board
import digitalio
import neopixel 

# Initialize the on-board neopixel and set the brightness.
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3

# Set up the IR Sensor using digital pin 2. 
ir_sensor = digitalio.DigitalInOut(board.D2)
ir_sensor.direction = digitalio.Direction.INPUT # Set the IR sensor as an input.
ir_sensor.pull = digitalio.Pull.UP              # Use the internal pull-up resistor.


# While loop runs the code inside continuously. 
while True:
    print(ir_sensor.value)
    if ir_sensor.value == False:
        led[0] = (255, 0, 0)
    if ir_sensor.value == True:
        led[0] = (0, 255, 0)
```

**Lastly, please end this section with a link to your code or file.**  

### Evidence
![ezgif-4-93d506e7f2](https://github.com/lwylie10/engr3/assets/143749987/521b2676-cebc-4610-b080-be3788dee529)
credit to Josh for the wiring
### Reflection
This assignment didn't really take me long at all because it was simple wiring the IR sensor up. I struggled for a bit on getter the ir sensor to read the right distance and send it back to the board on its own but once I figured it out everything worked. It would definielty be fun to make it change even more colors and play around with the settings on the sensor to make it even cooler.
## The Hanger🌾
### Assignment Description

Create the hanger part from the part's drawings in Onshape
### Evidence
![Part Studio 1](https://github.com/lwylie10/engr3/assets/143749987/aa534b2d-670c-4d9f-a3c9-2effd1606455)
![Part Studio 1 (1)](https://github.com/lwylie10/engr3/assets/143749987/90a9b0bd-836f-4378-a2e2-94b47c8e146b)
![Part Studio 1 (2)](https://github.com/lwylie10/engr3/assets/143749987/9439c5ba-0621-4006-9213-2da3b8a5c526)


### Part Link 

https://cvilleschools.onshape.com/documents/cb51d22aa62457813195827b/w/fd14b48316a7b15a5e5201a9/e/55beb68e2ef303168d330227?renderMode=0&uiState=651c6008b5a79f484def1c1a

### Reflection

At first I started to just draw the part based on looking at it from the front side which took a while because i had to use a three point arc. The part was overall not that hard because there weren't too many challenges to it, it was mostly just using lines to draw it, creating constraints, and then I finished with mirroring it over the center line. I really enjoy using the mirror tool because as long as it's symmetric, you only kind of have to do half of the work.

## Swing arm🌹
### Assignment Description
Make a swing arm from drawings provided
### Evidence
![Part Studio 1 (4)](https://github.com/lwylie10/engr3/assets/143749987/ea60f246-01bc-4756-8192-3ae312bae406)
![Part Studio 1 (3)](https://github.com/lwylie10/engr3/assets/143749987/4e140f96-c3fb-48ba-9dff-c001c9a0e557)

### Part Link 
https://cvilleschools.onshape.com/documents/d86e8a80871c06c2c8cee8dc/w/931ca79e48787292e18c4e8b/e/5876e6c59462faa80b29df9d?renderMode=0&uiState=651da6ebeaa442355009bb8f

### Reflection

The Swing Arm was definely harder then the hanger because it had a lot of complicated parts to it. I started off with drawing it on the front plan and sort of dimensioning it to get it mostly looking like how it should. Then i started extruding and I worked on the 3D parts that I couldn't draw. I struggled a lot to get the mass right once I changed the variables because I had a problem that I should've used the coincident tool instead of just dimensioning one thing to another part. I eventually fixed the variable problems and got the right mass by trial and error and using the rollback bar. 

## Multi-Part Cylinder Studios - Practice🌷
### Assignment Description

Create a multi-part shape in onshape based off of documents and then being able to change parts of the design which in turn affects the rest of the part
### Evidence

![Part Studio 1 (6)](https://github.com/lwylie10/engr3/assets/143749987/861f2974-cf86-447f-9fb8-844686672970)
Front View 
![Part Studio 1 (5)](https://github.com/lwylie10/engr3/assets/143749987/9a572e04-b9fd-4632-b169-ec41cd569fde)
Isometric View

### Part Link 

https://cvilleschools.onshape.com/documents/d8fb8aa520bb0bd546d988d3/w/f2aa70a75d91551ae9121758/e/1915032864752f764a7444b0?renderMode=0&uiState=6540015e32d8e777c5b6d3c6

### Reflection

This assignment took me a lot longer then it should have. I started off by not using the starting cylinder which definetly wasn't smart and it caused problems later in the design. I went down the line, creating the different parts based on each other and most of them didn't take too long. Once i hit the next couple questions, I struggled because not all of my dimensions worked correctly and they would break when I changed one of them. Next time I would definetly make sure to check all of my dimensions and also read the instructions more carefully because I totally missed the cylinder that it gave us in the beginning. I would also make sure that the dimenstions that were in parenthesis weren't incorperated into my design because it created problems for me later when I tried to change a part's dimension. I enjoyed this assignment a ton but it also showed me how fast I really will have to do this and I definetly need to study for the Onshape Certification exam. 

## Onshape Certification Prep 1: Single Part🪻
### Assignment Description

To practice for the Onshape exam and work more efficiently making single parts in Onshape. Create a single part from a drawing and dimensions.

### Evidence
![Part Studio 1 (7)](https://github.com/lwylie10/engr3/assets/143749987/25be1725-45b7-43db-a13b-4b192125a7a6)
Isometric View
![Part Studio 1 (8)](https://github.com/lwylie10/engr3/assets/143749987/ed7c88d3-2bf2-423d-a248-51e7bbbec4d9)
Front View
![Part Studio 1 (9)](https://github.com/lwylie10/engr3/assets/143749987/6174059b-d8ef-4a39-b7eb-ab606438bc9c)
Side View


### Part Link 

https://cvilleschools.onshape.com/documents/a688cd91fd45a4550313079a/w/9abaaa43fc1bcb2888b36522/e/244cbb91239fa99c23a4ec96?renderMode=0&uiState=654154cc1156cb60f7c28e1c

### Reflection

The assignment went mostly well. I started by drawing on the front view and drawing the general outline of the shape and then mirroring it over the center line. I think next time maybe I wont mirror it because it kinda created a couple problems later in the part. I then extruded the part and worked on the side view to create the bottom cutout which all worked fine. Everything was working until question 4 which then like everything broke because I had to change a TYP dimension and because I didn't create a variable and that might've fixed my problem later in the challenge. I got all of the questions right in the quiz and I only really need Miller's help for one of the questions. I need to be able to do it faster though. 

## Onshape Cert prep 3: Assemblies🌾
### Assignment Description

To practice for the Onshape exam and work more efficiently making single parts in Onshape. Create multiple parts and then put them together and be able to use variables to edit it even faster.

### Evidence
![Assembly 1 (2)](https://github.com/lwylie10/engr3/assets/143749987/eb1a8702-2126-443f-b91f-2cd479f57d23)
Isometric   
![Assembly 1](https://github.com/lwylie10/engr3/assets/143749987/ba7d11bc-f047-49a7-be04-ca04dca092da)
Front


### Part Link 

https://cvilleschools.onshape.com/documents/249b51e00b18b2ed06594e22/w/5bbd9abeeaa192062fbb4613/e/38a064fa93a6db56269ce032?renderMode=0&uiState=660316c5a1fd246156d321ee

### Reflection

In this assignment, I learned a couple of new ways to use mates such as the drop down menu which made editing the mates much easier. Its a super useful tool that I can use in the future to move my projects along faster. This project was a little challenging because of the different degrees i had to rotate the part and I also had to give it limits to make it so it doesn't extend too far and look really funky. I should've taken the first couple questions slower because it would've made the later questions easier because I would only have had to change like 2 things about it but instead i had to fix the problems I had created earlier.

## Onshape Cert prep 2: mic stand🌾
### Assignment Description
This assignment was to create a mic stand using a document to find all of the dimensions. We got a starting document which was the middle piece and then we had to build the mic holder and the pin off of that 

### Evidence
![Assembly 1 (4)](https://github.com/lwylie10/engr3/assets/143749987/a8a37feb-7028-4d00-a6ad-97b115d5d47c)
front 
![Assembly 1 (3)](https://github.com/lwylie10/engr3/assets/143749987/21ee6582-eaba-4770-a9dd-00968aec14ce)
isometric

### Part Link 

https://cvilleschools.onshape.com/documents/f482eb7c1fa0828924e43521/w/ba1c0b0c9518351ea879255d/e/49e601df17a4eca631d1b200?renderMode=0&uiState=660319ed5bf834338503febe

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

I think one of my biggest problems with this assignment was putting in dimensions that had parenthesis around them. This took a lot of my time because those dimensions in parethessi were supposed to be based off of the other parts and not dimensioned on their own. So when I had to change them later or use a variable to quickly change the value, it gave me a lot of problems which caused me to restart a couple of times and methodically read the instructions again. OVerall, it wasn't a hard assignment and as long as I checked each dimension and watched out for the parts that were based off of other parts, I can do this without much trouble

## Robot Gripper Design🌾
### Assignment Description

The assignment is to design a basic gripper for a robot arm. The requirements are:
The gripper must close using only one actuator (one servo, one solenoid, one motor, etc)
The jaws of the gripper must be able to fully close.
All parts of the gripper must be able to be 3D printed, laser cut, or already exist in the engineering lab
The gripper must be fully assembled in Onshape with all fasteners, and the assembly must be able to be animated

### Evidence
![Assembly 1 (6)](https://github.com/lwylie10/engr3/assets/143749987/5a61101d-1fa6-49c9-bd45-58e30772d617)
front
![Assembly 1 (5)](https://github.com/lwylie10/engr3/assets/143749987/0126094f-ae51-46d2-bf25-00419eb596ca)
isometric

### Part Link 

https://cvilleschools.onshape.com/documents/d1b222726e077da5b586d846/w/3e2749127f53dd8ce50686ed/e/0005d5029271e50db13bad28?renderMode=0&uiState=66031d3b4be58203d78bc0c1

### Reflection

Ok... This was either a very hard assignment or I'm just a total idiot. It started out super well! The errors I had I kinda ignored and kept going and I had most of the parts built off of each other(mistake). It was all fine until I tried to mirror it over the y axis to make the part 3D. Thats when literally everything broke. I swear one error led to another and I didn't even know where to start to fix it. Luckily Benji came to the rescue and gave me a bunch of tips on how to fix it and also make sure it doesn't happen next time. One thing that I was doing wrong was that I made the parts and built them off of each other so instead I built them individually and mirrored it even more to make sure all of my dimensions were correct on both sides. Overall, once I got some tips from Benji, I was able to fix the project and get it working.

## Onshape_Assignment_Template🌾
### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence

Take several cropped screenshots of your Onshape document from different angles. Try to capture all important aspects of the design. Turn off overlays that obscure the parts, such as planes or mate connectors. Your images should have captions, so the reader knows what they are looking at!  

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!
## NextAssignment

### Description & Code Snippets
Write a couple sentences here, describing this assignment, and make sure that you hit these two points:
* What was the goal of the assignment?
* How did you accomplish that goal?
  How you accomplished the goal is NOT a reflection, it is you telling the reader how to do this assignment, in broad strokes.

  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  

### Evidence

### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)
### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**

