#!/usr/bin/env pybricks-micropython
# Aaditya and Ishaan code here.
from ColorSensorFunctions import *
from GradualGyroB import *
from GradualGyroF import *
from TurnGradualGyro import *

# ORIGINALLY RUN 2 
# RYAN CHANGED IT TO RUN 1 ON 1/3/20

readAllValues()
def Run1():
    gradualGyroBackward(200, 100)
    turnGradualGyro(12)
    gradualGyroBackward(116,90)
    turnGradualGyro(-12)
    turnGradualGyro(12)
    robot.stop(Stop.COAST)
    gradualGyroForward(20, 100)
    turnGradualGyro(-2)
    gradualGyroBackward(110, 60)
    gradualGyroForward(270, 100)
    turnGradualGyro(44)
    gradualGyroBackward(680, 100)
    #stopOnWhiteSRun2()
    #stopOnBlackB()
    #turnGradualGyro(-10)
    turnGradualGyro(13)
    gradualGyroForward(110, 100)
    turnGradualGyro(-70)
    #sideLineFollowerRun2(50)
    gradualGyroBackward(300, 100)
    gradualGyroForward(50, 100)


# Run1()