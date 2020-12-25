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
    gradualGyroBackward(108,90)
    turnGradualGyro(-15)
    turnGradualGyro(15)
    robot.stop(Stop.COAST)
    gradualGyroForward(20, 100)
    turnGradualGyro(-2)
    gradualGyroBackward(105, 60)
    gradualGyroForward(270, 100)
    turnGradualGyro(50)
    gradualGyroBackward(320, 100)
    stopOnBlackB()
    turnGradualGyro(-14)
    gradualGyroBackward(180, 100)
    turnGradualGyro(21)
    gradualGyroForward(120, 100)
    #stopOnBlackFRun2()
    turnGradualGyro(-55)
    gradualGyroBackward(105, 100)
    #stopOnBlackSRun2()
    turnGradualGyro(-18)
    sideLineFollowerRun2(50)
    backLineFollowe(50)


Run2()