#!/usr/bin/env pybricks-micropython

from robot import *

def stopOnBlackFront():
    #global p3FSensor
    print("Front color reflection: " + str(p3FSensor.reflection()))
    while p3FSensor.reflection() > 20:
        theRobot.drive(50, 0)
    theRobot.stop(Stop.BRAKE)

