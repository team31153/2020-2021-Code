#!/usr/bin/env pybricks-micropython

from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *

readAllValues()

def Run3Pt2():
    turnGradualGyro(30)
    gradualGyroForward(40, 40)
    turnGradualGyro(-30)
    gradualGyroBackward(500, 100)

Run3Pt2()