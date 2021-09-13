# Write your code here :-)

import board
import time
import neopixel
import pwmio
import servo

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
pwm = pwmio.PWMOut(board.A2, duty_cycle=2**15, frequency=200)
super_snazzy_servo = servo.Servo(pwm)
purple = [146, 0, 199]
orange = [255, 50, 0]
dot.brightness = 0.1
while True:
    for angle in range(0, 180,2):
        dot.fill((purple))
        print("Going fowards!")
        super_snazzy_servo.angle = angle
        time.sleep(0.05)

    for angle in range(180, 0, -2):
        dot.fill((orange))
        print("Coming back!")
        super_snazzy_servo.angle = angle
        time.sleep(0.05)
