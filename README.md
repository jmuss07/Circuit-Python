# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
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
Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring
No wiring, all you need is and Adafruit Metro Express

### Reflection
This one worked well, and was pretty easy once I figured out the basic Cicuit Python commands. I then went




## CircuitPython_Servo

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
