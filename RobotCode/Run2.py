#!/usr/bin/env pybricks-micropython
# Aaditya and Ishaan code here.
from ColorSensorFunctions import *
from GradualGyroB import *
from GradualGyroF import *
from TurnGradualGyro import *
def Run2():
    gradualGyroBackward(200, 100)
    turnGradualGyro(10)
    gradualGyroBackward(120,60)
    turnGradualGyro(-15)
    turnGradualGyro(15)
    robot.stop(Stop.COAST)
    gradualGyroBackward(130, 20)
    gradualGyroForward(150, 100)
    turnGradualGyro(90)
    gradualGyroBackward(500, 100)
    


Run2()