# Write your code here :-)
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
