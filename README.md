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

## Hello_CircuitPython

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

## CircuitPython_Servo

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


## Circuit_Python_Distance_Sensor

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

## Motor_Control

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




## Photointeruppter

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
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)
### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**


## The Hanger

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

## Swing arm

### Assignment Description
Make a swing arm from drawings provided
### Evidence
![Part Studio 1 (4)](https://github.com/lwylie10/engr3/assets/143749987/ea60f246-01bc-4756-8192-3ae312bae406)
![Part Studio 1 (3)](https://github.com/lwylie10/engr3/assets/143749987/4e140f96-c3fb-48ba-9dff-c001c9a0e557)

### Part Link 
https://cvilleschools.onshape.com/documents/d86e8a80871c06c2c8cee8dc/w/931ca79e48787292e18c4e8b/e/5876e6c59462faa80b29df9d?renderMode=0&uiState=651da6ebeaa442355009bb8f

### Reflection

The Swing Arm was definely harder then the hanger because it had a lot of complicated parts to it. I started off with drawing it on the front plan and sort of dimensioning it to get it mostly looking like how it should. Then i started extruding and I worked on the 3D parts that I couldn't draw. I struggled a lot to get the mass right once I changed the variables because I had a problem that I should've used the coincident tool instead of just dimensioning one thing to another part. I eventually fixed the variable problems and got the right mass by trial and error and using the rollback bar. 

## Multi-Part Design Studios - Practice

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

## Onshape Certification Prep 1: Single Part

### Assignment Description

To practice for the Onshape exam and work more efficiently making single parts in Onshape.

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

## Alignment Plate

### Assignment Description

Create the alignment plate on the cad challenges

### Evidence
![Part Studio 2](https://github.com/lwylie10/engr3/assets/143749987/6415a147-bdc5-4f3a-bb6d-be67e35497d1)
isometric
![Part Studio 2 (1)](https://github.com/lwylie10/engr3/assets/143749987/3b725288-2fdf-456a-b43c-1c7901182d3f)
front

### Part Link 

https://cvilleschools.onshape.com/documents/cc6589a8c5b26f47e8434221/w/7d595a653a6c51d2beacefcc/e/6d1eaef25ef5e55bcc93c994?renderMode=0&uiState=654befd784c4093ec77c7bf0

### Reflection

This assignment was incredibly easy and it took me less then 10 minutes. I started by drawing a rectangle then I drew the circles into the sides of the rectangle where the drawings said they went. One thing i forgot to do was make sure the circle's dimensions were in diameter because the drawing gave me the radius and I forgot to multiply it by 2. I would probably start by mirroring the entire thing next time because it would make changing one side of the piece easier.   

## Onshape_Assignment_Template

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

