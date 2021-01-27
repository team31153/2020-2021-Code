#!/usr/bin/env pybricks-micropython
from Run1 import *
from Run2 import *
from Run3 import *
from Run3MK2 import *
from Run3MK3 import *
from Run3MK4 import *
from Run3MK5 import *

# Write your program here.
#Calls functions imported from programs

def waiting():
    ev3.light.off()
    ev3.screen.clear()
    ev3.screen.draw_text(0, 50, "Choose a")
    ev3.screen.draw_text(0, 70, "program")

readAllValues()
waiting()
while True:

    listOfButtons = ev3.buttons.pressed()
    for oneButton in listOfButtons:
        print(oneButton)
        if oneButton == Button.CENTER: 
            ev3.light.on(Color.RED)
            ev3.screen.clear()
            ev3.screen.draw_text(0, 50, "RUN 3 MK3")
            Run3MK3()
            waiting()

        if oneButton == Button.UP:
            ev3.light.on(Color.GREEN)
            ev3.screen.clear()
            ev3.screen.draw_text(0, 50, "RUN 1")
            Run1()
            waiting()
    
        if oneButton == Button.RIGHT:
            ev3.light.on(Color.ORANGE)
            ev3.screen.clear()
            ev3.screen.draw_text(0, 50, "RUN 2")
            Run2()
            waiting()

        if oneButton == Button.DOWN:
            ev3.light.on(Color.RED)
            ev3.screen.clear()
            ev3.screen.draw_text(0, 50, "RUN 3")
            Run3MK4()
            ev3.light(None)
            waiting()

        if oneButton == Button.LEFT:
            ev3.light.on(Color.RED)
            ev3.screen.clear()
            ev3.screen.draw_text(0, 50, "RUN 3 MK2")
            Run3MK5()
            waiting()
