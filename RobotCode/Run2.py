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
    gradualGyroBackward(115,60)
    turnGradualGyro(-16)
    turnGradualGyro(15)
    robot.stop(Stop.COAST)
    gradualGyroForward(20, 30)
    gradualGyroBackward(130, 20)
    gradualGyroForward(250, 100)
    turnGradualGyro(48)
    gradualGyroBackward(150, 100)
    stopOnBlackB()


Run2()