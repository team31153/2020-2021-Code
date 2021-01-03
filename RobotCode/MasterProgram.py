#!/usr/bin/env pybricks-micropython
from Run1 import *
from Run2 import *
from Run3 import *

# Write your program here.
#Calls functions imported from programs

def waiting():
    ev3brick.light(None)
    ev3.screen.clear()
    ev3.screen.draw_text(0, 50, "Choose a")
    ev3.screen.draw_text(0, 70, "program")


while True:

    listOfButtons = ev3.buttons.pressed()
    for oneButton in listOfButtons:
        print(oneButton)
        waiting()
        if oneButton == Button.CENTER: 
            waiting()

        if oneButton == Button.UP:
            ev3brick.light(Color.GREEN)
            ev3.screen.clear()
            ev3.screen.draw_text(0, 50, "RUN 1")
            Run1()
            waiting()
    
        if oneButton == Button.RIGHT:
            ev3brick.light(Color.ORANGE)
            ev3.screen.clear()
            ev3.screen.draw_text(0, 50, "RUN 2")
            Run2()
            waiting()

        if oneButton == Button.DOWN:
            ev3brick.light(Color.RED)
            ev3.screen.clear()
            ev3.screen.draw_text(0, 50, "RUN 3")
            Run3()
            ev3brick.light(None)
            waiting()

        if oneButton == Button.LEFT:
            waiting()
