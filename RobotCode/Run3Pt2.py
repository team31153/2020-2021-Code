#!/usr/bin/env pybricks-micropython

from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *

readAllValues()

def run3Pt2():
    turnGradualGyro(30)
    gradualGyroForward(30, 40)
    turnGradualGyro(-22)
    gradualGyroBackward(750, 100)

#Run3Pt2()