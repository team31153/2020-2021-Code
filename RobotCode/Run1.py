#!/usr/bin/env pybricks-micropython
# Aaryan and Felix code here.
from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *
from GyroB import *
from GyroF import *

readAllValues()

# Code Here.
def Run1():

    gradualGyroForward(780, 135)
    wait(10)
    gradualGyroForward(200, 25)
    robot.straight(-90)
    robot.turn(110)
    robot.straight(150)
    robot.turn(-80)
    frontLineFollowerStopWithSide(65)

Run1()