#!/usr/bin/env pybricks-micropython
# Aaditya and Ishaan code here.
from ColorSensorFunctions import *
from GradualGyroB import *
from GradualGyroF import *
from TurnGradualGyro import *

readAllValues()

def Run2():
    # Write Code Here:
    #gradualGyroBackward(320, 90)
    aMotor.run_angle(10000, 3000)

Run2()