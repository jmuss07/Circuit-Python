# CircuitPython
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [Ultrasonic Sensor](#Ultrasonic_Sensor)
* [CircuitPython Photointerrupter](#CircuitPython_Photointerrupter)
* [CircuitPython_LCD](#CircuitPython_LCD)

---

## Hello_CircuitPython

### Description & Code
The code makes the Neopixel on the Metro Express flash a random color from a list of rainbow colors. It's looped so that every 0.1 seconds it chooses a different color from the same list.

```python
# Write your code here :-)
#This is Josie's pride and joy
import board
import neopixel
import time
import random

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

red = [204, 0, 0]
orange = [255, 50, 0]
yellow = [200, 100, 0]
green = [0, 230, 0]
blue = [0, 0, 255]
purple = [146, 0, 199]
color_list = [red, orange, yellow, green, blue, purple]
print("Make it disco!!!")
dot.brightness = 0.1
while True:
    random_color = random.choice(color_list)
    dot.fill((random_color))
    time.sleep(0.1)


```


### Evidence
Look at it go!! So many random colors...

![Look at it go!! So many random colors...](https://github.com/jmuss07/Circuit-Python/blob/main/Images/Random_Color.gif?raw=true)

### Wiring
No wiring, all you need is and Adafruit Metro Express

### Reflection
This one worked well, and was pretty easy once I figured out the basic Cicuit Python commands. I then went through and decided to switch from just the required LED color change to experimenting with lists in order to achieve the final product. 




## CircuitPython_Servo

### Description & Code
This servo is powered via capacitive touch! (If you touch one wire, it turns one way, and if you touch the other the servo spins the other way!)

```python
# Write your code here :-)

import board
import time
import pwmio
import servo
import touchio

touch_a4 = touchio.TouchIn(board.A4) #your basic capacitive touch command!
touch_a0 = touchio.TouchIn(board.A0)

pwm = pwmio.PWMOut(board.A2, duty_cycle=2**15, frequency=200) #sets the servo rotation frequency
super_snazzy_servo = servo.Servo(pwm) #simplifies servo function by setting it equal to the desired frequency

super_snazzy_servo.angle = 90 #sets your starting servo angle
angle = 90 #Sets your starting value for angle

while True:
    if touch_a4.value: #If function for the first capacitive touch value, this one will control fowards motion
        print("Going fowards!")
        if angle in range(0, 175): #Making sure that the angle is in a viable range to continue moving
            angle += 5 #Adds value to the initial angle value (Set on the first line above the while true statement)
            super_snazzy_servo.angle = angle #Sets servo angle to our new angle value
            print(angle) #Tells us our new angle value on the serial monitor
        time.sleep(0.05) #Sets a rest interval before continuing the loop

    if touch_a0.value: #If function for the second capacitive touch value, this one will control backwards motion
        print("Coming back!")
        if angle in range(5, 180):#Making sure that the angle is in a viable range to continue moving
            angle -= 5 #Subtracts value from the initial angle value (Set on the first line above the while true statement)
            super_snazzy_servo.angle = angle #Sets servo angle to our new angle value
            print(angle) #Tells us our new angle value on the serial monitor
            time.sleep(0.05)  #Sets a rest interval before continuing the loop
  
  if not touch_a4.value and not touch_a0.value: #Checks if no wires are touched so that code doesn't go into a paniced 
        print("I'm no longer moving (help!)") #Lets us know via the serial monitor that the servo is not moving (that the capcitive touch isn't recieving input)
        time.sleep(.05)  #Sets a rest interval before continuing the loop

    time.sleep(.05)  #Sets a rest interval before continuing the loop


```

### Evidence
The servo itself working with capacitive touch...

![The servo itself working with capacitive touch...](https://github.com/jmuss07/Circuit-Python/blob/main/Images/Servo_GIF.gif?raw=true)

...And the serial moniter showing its rotations!

![...And the serial moniter showing its rotations!](https://github.com/jmuss07/Circuit-Python/blob/main/Images/Servo_Code_GIF.gif?raw=true)
### Wiring
Simple servo wiring!

![Simple servo wiring!](https://github.com/jmuss07/Circuit-Python/blob/main/Images/servo.png?raw=true)

### Reflection
This one was a lot more challenging. Although I was able to get the servo code and capacitive touch code to work well independently, actually combining the two parts proved to be diffiucult. After a lot of trouble shooting, I was final;ly able to get it to work well!


## Ultrasonic_Sensor

### Description & Code
This code powers an HCSR04 ultrasonic sensor. As the distance changes, the built in LED (the neopixel) on a Metro Express gradually shifts in colors in a range from red to green.

```python

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel
import adafruit_hcsr04 #imports ultrasonic sensor
import simpleio #imports map function library

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D8, echo_pin=board.D9) #sets ultrasonic sensor pins
distance = 0
dot.brightness = 0.1
while True:
    try:
        distance = sonar.distance #sets the variable "distance" to equal the number the ultrasonic sends back
        print((distance,)) #prints the numeric value of distance
    except RuntimeError: #Use if the ultrasonic does not recieve input
        print("Retrying!") #report error message to the serial monitor
    time.sleep(0.1)

    if distance >= 5 and distance < 20: #Sets a range for the distance
        blue = int(simpleio.map_range(distance, 5, 20, 0, 255)) #Maps out the values of blue that the led moves between
        green = int(simpleio.map_range(distance, 5, 20, 0, 0)) #Maps out the values of green that the led moves between
        red = int(simpleio.map_range(distance, 5, 20, 255, 0)) #Maps out the values of red that the led moves between
        dot.fill((red, green, blue)) #Changes the led color to equal the new values for red,green and blue

    if distance >= 20 and distance < 35: #Sets a range for the distance
        blue = int(simpleio.map_range(distance, 20, 35, 255, 0))  #Maps out the values of blue that the led moves between
        green = int(simpleio.map_range(distance, 20, 35, 0, 255)) #Maps out the values of green that the led moves between
        red = int(simpleio.map_range(distance, 20, 35, 0, 0))  #Maps out the values of red that the led moves between
        dot.fill((red, green, blue)) #Changes the led color to equal the new values for red,green and blue
```

### Evidence
It works!

![It works!](https://github.com/inovotn04/CircuitPython/raw/main/Images/DistanceSensorEvidence.gif?raw=true)

Image credit goes to [Ian Novotne](https://github.com/inovotn04/CircuitPython)

### Wiring
Ultrasonic sensor wiring!
![Ultrasonic sensor wiring!](https://github.com/Jhouse53/CircuitPython/raw/main/GIF%20and%20Images/UltraSonicSensor%20wiring.PNG?raw=true)

Image credit goes to [Benton House](https://github.com/Jhouse53/CircuitPython)
### Reflection
This one was a lot more challenging. It was a struggle to get my ultrasonic sensor code to work on its own, though I eventually figured out that that problem was being caused purely because the sensor I was using was broken. Once I switched it out to a working sensor, the code worked well. The next challenge came with coding the light. While I originally attempted coding the gradually color shifting LED
using math, that strategy didn't work in the end and proved to be extremely dsifficult. As such, I switched to using a new method known as color mapping. Once I figured out how this worked, the LED worked well.



## CircuitPython_Photointerrupter

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring
Photointerrupter wiring!
![Photointerrupter wiring!](https://github.com/jmuss07/Circuit-Python/blob/main/Images/Photointerrupter.PNG?raw=true)

### Reflection





## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection




