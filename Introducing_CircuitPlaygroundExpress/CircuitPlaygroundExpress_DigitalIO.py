# CircuitPlaygroundExpress_DigitalIO

import time

import board
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

buttonA = DigitalInOut(board.BUTTON_A)
buttonB = DigitalInOut(board.BUTTON_B)
switch = DigitalInOut(board.SLIDE_SWITCH)
buttonA.direction = Direction.INPUT
buttonB.direction = Direction.INPUT
switch.direction = Direction.INPUT
buttonA.pull = Pull.DOWN
buttonB.pull = Pull.DOWN
switch.pull = Pull.UP

while True:
    if buttonA.value and buttonB.value and switch.value:  # button is pushed
        led.value = True
    else:
        led.value = False
