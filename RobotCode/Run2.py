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
    gradualGyroBackward(110,80)
    turnGradualGyro(-15)
    turnGradualGyro(15)
    robot.stop(Stop.COAST)
    gradualGyroForward(20, 30)
    #turnGradualGyro(-1)
    gradualGyroBackward(110, 20)
    gradualGyroForward(250, 100)
    turnGradualGyro(49)
    gradualGyroBackward(150, 100)
    stopOnBlackB()
    turnGradualGyro(-14)
    gradualGyroBackward(180, 100)
    turnGradualGyro(20)
    gradualGyroForward(150, 100)
    #stopOnBlackFRun2()
    turnGradualGyro(-55)
    gradualGyroBackward(120, 100)
    stopOnBlackSRun2()
    turnGradualGyro(-10)
    sideLineFollowerRun2(20)


Run2()