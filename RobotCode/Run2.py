#!/usr/bin/env pybricks-micropython
# Aaditya and Ishaan code here.
from ColorSensorFunctions import *
from GradualGyroB import *
from GradualGyroF import *
from TurnGradualGyro import *

readAllValues()
def Run2():
    gradualGyroBackward(200, 100)
    turnGradualGyro(12)
    gradualGyroBackward(115,90)
    turnGradualGyro(-15)
    turnGradualGyro(15)
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
    turnGradualGyro(-60)
    sideLineFollowerRun2(50)


Run2()