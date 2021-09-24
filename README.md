# CircuitPython
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
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



## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection




