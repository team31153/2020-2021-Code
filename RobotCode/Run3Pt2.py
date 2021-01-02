#!/usr/bin/env pybricks-micropython

from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *

readAllValues()

def run3Pt2():
    # gradualGyroForward(30, 40)
    # turnGradualGyro(-31)
    robot.straight(350)
    gradualGyroBackward(710, 200)


#Run3Pt2()