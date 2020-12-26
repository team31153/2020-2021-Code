#!/usr/bin/env pybricks-micropython
from Initialize import *

while True:

    listOfButtons = ev3.buttons.pressed()
    for oneButton in listOfButtons:
        if oneButton == Button.UP:
            aMotor.run_angle(10000, 4500)
        if oneButton == Button.RIGHT:
            bMotor.run_angle(1000, 2700)
        if oneButton == Button.DOWN:
            aMotor.run_angle(10000, -4500)
        if oneButton == Button.LEFT:
            bMotor.run_angle(1000, -2700)
        