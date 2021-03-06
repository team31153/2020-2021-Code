#!/usr/bin/env pybricks-micropython
# Aaditya and Ishaan code here.
from ColorSensorFunctions import *
from GradualGyroB import *
from GradualGyroF import *
from TurnGradualGyro import *

# ORIGINALLY RUN 2 
# RYAN CHANGED IT TO RUN 1 ON 1/3/20

# readAllValues()
def Run1():
    gradualGyroBackward(230, 150)
    turnGradualGyro(12)
    gradualGyroBackward(105,90)

    turnGradualGyro(-12)
    turnGradualGyro(12)
    robot.stop(Stop.COAST)
    gradualGyroForward(20, 100)
    turnGradualGyro(-1)
    gradualGyroBackward(110, 60)
    gradualGyroForward(270, 300)
    turnGradualGyro(43)
    gradualGyroBackward(570, 250)
    #turnGradualGyro(13)
    #gradualGyroForward(110, 200)
    turnGradualGyro(-66)
    #sideLineFollowerRun2(50)
    gradualGyroBackward(250, 300)
    gradualGyroBackward(70, 100)
    gradualGyroForward(130, 100)
    turnGradualGyro(-54)
    gradualGyroBackward(680, 275)
    robot.turn(180)
    gradualGyroBackward(300, 250)



#Run1()