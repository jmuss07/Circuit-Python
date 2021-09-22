
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel
import adafruit_hcsr04
import simpleio

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D8, echo_pin=board.D9)
distance = 0
dot.brightness = 0.1
while True:
    try:
        distance = sonar.distance
        print((distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)

    if distance >= 5 and distance < 20:
        blue = int(simpleio.map_range(distance, 5, 20, 0, 255))
        green = int(simpleio.map_range(distance, 5, 20, 0, 0))
        red = int(simpleio.map_range(distance, 5, 20, 255, 0))
        dot.fill((red, green, blue))

    if distance >= 20 and distance < 35:
        blue = int(simpleio.map_range(distance, 20, 35, 255, 0))
        green = int(simpleio.map_range(distance, 20, 35, 0, 255))
        red = int(simpleio.map_range(distance, 20, 35, 0, 0))
        dot.fill((red, green, blue))

