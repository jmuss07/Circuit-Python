# Write your code here :-)
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
