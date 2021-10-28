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
This one worked well, and was pretty easy once I figured out the basic Cicuit Python commands, which are somewhat similar to those used by Arduino, though there all some differences (for instance, you don't need semicolons at the end of each line, and different commands vary; "While True:" statementds are loops). I then went through and decided to switch from just the required LED color change to experimenting with lists in order to achieve the final product. 




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
This one was a lot more challenging. It turns out that the code for a servo is a lot different in Circuit Python as opposed to Arduino. This was my first time using the "pwmio" funtion. The "pwmio" function controls the servo and uses frequency cycles. When using this function, I found out that I should use a cycle of "2* * 15" and a frequency of 200. I had never coded capcitive touch before, so I started out with a search for what it is. My original code for capacitive touch was controled by plugging the wire in and out, whereas capacitive touch is meant to be controlled by touching different wires with your finger. When I found that out, I did a bit more research and adjusted the code a bit until I could get the capcitive touch code to sork on it's own (Touching one wire printed a message to the serial moniter, and touching the other printed a different message). Although I was able to get the servo code and capacitive touch code to work well independently, actually combining the two parts proved to be diffiucult. After a lot of trouble shooting and more research, I found out that the problem came from my syntax and conflicting "if" statements. In order for the code to work, you need to make sure that you put the "if" statement for servo rotation ***inside*** the corresponding "If" loop for the capacitive touch code. You also need to make a third "If" statement for if no wire is touched, so that the servo only turns if it's triggered by the touch of a wire.

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
This one was a lot more challenging. It was a struggle to get my ultrasonic sensor code to work on its own, though I eventually figured out that that problem was being caused purely because the sensor I was using was broken. Once I switched it out to a working sensor, the code worked well. The next challenge came with coding the light. While I originally attempted coding the gradually color shifting LED using math, that strategy didn't work in the end and proved to be extremely dsifficult. As such, I switched to using a new method known as color mapping. I had to do some research on it before using it, but I found that color mapping does the math for you. You simply give it two values and a time cycle, and it wsill do the work of shifting the numbers as needed! Once I figured out how this worked, the LED worked well.



## CircuitPython_Photointerrupter

### Description & Code
This code utilises a photointerrupter. The serial moniter prints out the number of times the photointerrupter is interrupted, and it resets back to 0 interrupts every four seconds.
```python
import board
import time
import digitalio

interrupter_pin = digitalio.DigitalInOut(board.D8)
interrupter_pin.switch_to_input
interrupter_pin.pull = digitalio.Pull.UP

initial_time = time.monotonic()
photo = False
state = False

counter = 0
max = 4
while True:
    photo = interrupter_pin.value
    if photo and not state:
        counter += 1
        print(str(counter))

    state = photo

    new_time = max - time.monotonic()

    if new_time <= 0:
        print(str(counter))
        max = time.monotonic() + 4
        counter = 0
```

### Evidence

The photointerrupter itself being triggered...

![The photointerrupter itself being triggered...](https://github.com/jmuss07/Circuit-Python/blob/main/Images/Photointerrupter_GIF.gif?raw=true)

...And the serial moniter showing the number of interruptions!

![...And the serial moniter showing the number of interruptions!](https://github.com/jmuss07/Circuit-Python/blob/main/Images/Photointerrupter_Code_GIF.gif?raw=true)

### Wiring
Photointerrupter wiring!

![Photointerrupter wiring!](https://github.com/jmuss07/Circuit-Python/blob/main/Images/Photointerrupter.PNG?raw=true)

### Reflection
I ran into some challenges originally, since I had never worked with a photointerrupters before. You can use the photointerrupter by setting a time frequency and a counter, and I figured out how to operate the "Photo" command through the Arduino website This code also utilises time.monotonic instead of time.sleep, which I had never used before. However, I found that both functions are fairly similar, with only slight differnces in command sentences. A quick Google search showed me the correct phrasing (Which I used in my code above!). Once I got the photointerrupter to successfully record the number of interrupts, the next challenge came from trying to get it to not only reset back to 0 interrupts every four seconds, but also to have it print out that number every second. I figured out that this is where the counter, time.monotonic, and string statements came in handy, and created a new if statement that said that if the internal time recorded by time.monotonic was greater than or equal to 4, both the timer and the counter would reset to zero. Once I got it to work and did some research on photointerrupters and the time.monotonic function, the code made a lot of sense.




## CircuitPython_LCD

### Description & Code
Two wires use capacitive touch, with one determining whether it was counting up or down and the other registering and recording/counting the number of touches. The LCD screen displays what number the counter is at.

```python
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import touchio

touch_a4 = touchio.TouchIn(board.A4) 
touch_a1 = touchio.TouchIn(board.A1)
jeff = 1   
# jeff is just what I named my variable that controls whether its counting up or down
counter = 0 
# The number of touches registered
joe = 0 
# A boolean that registers one prolonged
# touch of the wire as just a single touch as opposed to mulitple
frank = 0 
# A boolean that registers one prolonged 
# touch of the wire as just a single touch as opposed to mulitple

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

lcd.print("I have gained   sentience!! :)")

while True:

    if touch_a1.value and frank == 0:  
        # If frank is not zero, it will register as multiple touches instead of just one
        print("touch a1")  # prints to serial moniter
        jeff = -jeff  
        # reverse the sign of jeff; changes from counting up to counting down or vice versa
    frank = touch_a1.value  
    # resets frank so that it doesn't register as multiple touches

    if jeff <= 0 and touch_a4.value and joe == 0:
        # If joe is not zero, it will register as multiple touches instead of just one
        # If jeff is less than or equal to zero, that means that it's counting down
        print("touch a4")  # prints to the serial moniter
        lcd.set_cursor_pos(0, 0)  # clears the LCD screen
        counter += jeff  # Adds the value of jeff (In this case -1) to the counter
        lcd.print("Counting down!:P")  
        # Prints to the LCD screen a message that it's counting down
        lcd.print("Value:")
        # Prints a message to the LCD screen on a seperate line
        lcd.print(str(counter))
        # Prints the current value of the counter to the LCD screen
        lcd.print(str(" "))
        # Prints an extra space to the LCD screen
    joe = touch_a4.value
    # resets joe so that it doesn't register as multiple touches
    
    if jeff >= 0 and touch_a4.value and joe == 0:
        # If joe is not zero, it will register as multiple touches instead of just one
        # If jeff is greater than or equal to zero, that means that it's counting up
        print("touch a4")  # prints to the serial moniter
        lcd.clear()  # clears the LCD screen
        counter += jeff  # Adds the value of jeff (In this case 1) to the counter
        lcd.print("Counting up! >_<")
        # Prints to the LCD screen a message that it's counting up
        lcd.print("Value:")
        # Prints a message to the LCD screen on a seperate line
        lcd.print(str(counter))
        # Prints the current value of the counter to the LCD screen
    joe = touch_a4.value
        # resets joe so that it doesn't register as multiple touches


```

### Evidence
It works!

![It works!](https://github.com/jmuss07/Circuit-Python/blob/main/Images/LCD_GIF.gif?raw=true)

### Wiring
LCD screen wiring!

![LCD screen wiring!](https://github.com/jmuss07/Circuit-Python/blob/main/Images/LCD.PNG?raw=true)
### Reflection
I had some trouble getting the screen to clear quickly enough, and for all the text to fit and still be fast. At first, I did the assignment wrong so that one wire counted up and the other counted down. In addition, when I touched and held one wire, it continued to count, registering it as many rapid touches instead of one long one. I had to do some research on what was causing the issue, and I managed to find out that something called "Booleans" (which work similar to true-false statements) would help to fix the issue. I'm still not the most sure about how booleans work, but I have a better understanding of it now that I've finished this assignment. Once I got the hang of booleans, the correct effect was easier to accomplish. However, the assignment was to have one wire control whether it was counting up or down, and then other would change the numbers/register and record each touch. Getting the wire that controled whether it was counting up or down was hard, and I had to employ yet another boolean that determined whether the following numbers were poositive or negative. Another challenge came from faulty wires and a slow clear time on the LCD screen, but I was able to fix the clear time issue with the command "lcd.set_cursor_pos(0, 0) ".



