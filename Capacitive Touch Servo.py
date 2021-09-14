# Write your code here :-)

import board
import time
import pwmio
import servo
import touchio

touch_a4 = touchio.TouchIn(board.A4)
touch_a0 = touchio.TouchIn(board.A0)

pwm = pwmio.PWMOut(board.A2, duty_cycle=2**15, frequency=200)
super_snazzy_servo = servo.Servo(pwm)

super_snazzy_servo.angle = 90
angle = 90

while True:
    if touch_a4.value:
        print("Going fowards!")
        if angle in range(0, 175):
            angle += 5
            super_snazzy_servo.angle = angle
            print(angle)
        time.sleep(0.05)

    if touch_a0.value:
        print("Coming back!")
        if angle in range(5, 180):
            angle -= 5
            super_snazzy_servo.angle = angle
            print(angle)
            time.sleep(0.05)
    if not touch_a4.value and not touch_a0.value:
        print("I'm so lonely")
        time.sleep(.05)

    time.sleep(.05)