#!/usr/bin/env pybricks-micropython
# Aaditya and Ishaan code here.
from ColorSensorFunctions import *
from GradualGyroB import *
from GradualGyroF import *
from TurnGradualGyro import *
def Run2():
    gradualGyroBackward(200, 100)
    turnGradualGyro(10)
    gradualGyroBackward(190,70)
    turnGradualGyro(-15)
    turnGradualGyro(15)
    gradualGyroBackward(120, 30)


Run2()