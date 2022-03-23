import time
import board
from rgb import LED

redPin = board.D7
bluePin = board.D5
greedPin = board.D6
redPin2 = board.D4
greedPin2 = board.D3
bluePin2 = board.D8

red = LED(redPin)
blue = LED(bluePin)
greed = LED(greedPin)
red2 = LED(redPin2)
greed2 = LED(greedPin2)
blue2 = LED(bluePin2)

while True:
    red.on(35000)
    greed.fade()
    blue.off()
    red2.on(15000)
    greed2.off()
    blue2.fade()