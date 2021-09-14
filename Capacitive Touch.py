# Write your code here :-)
import time
import board
import touchio

touch_a4 = touchio.TouchIn(board.A4)
touch_a5 = touchio.TouchIn(board.A5)

while True:
    if touch_a4.value:
        print("Touched A4!!")
        time.sleep(0.5)

    if touch_a5.value:
        print("Touched A5!!")
        time.sleep(0.5)