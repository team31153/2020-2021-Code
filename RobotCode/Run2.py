#!/usr/bin/env pybricks-micropython
# Aaditya and Ishaan code here.
from ColorSensorFunctions import *
from GradualGyroB import *
from GradualGyroF import *
from TurnGradualGyro import *

readAllValues()

def Run2():
    # Write Code Here:
    gradualGyroBackward(200, 100)
    turnGradualGyro(26)
    gradualGyroBackward(150,50)
    turnGradualGyro(-10)
    gradualGyroForward(100, 50)
    turnGradualGyro(-20)
    gradualGyroBackward(150, 30)
    turnGradualGyro(6)
    aMotor.run_angle(10000, -5000)
    gradualGyroForward(70, 90)
    turnGradualGyro(-20)

Run2()