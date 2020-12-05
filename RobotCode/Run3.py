#!/usr/bin/env pybricks-micropython

from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *

def Run3():

    colorSensorValuesInitialized = False

    # Get out of base to go on line
    gradualGyroBackward(200, 100)
    # Line follows
    print("before line follower")
    backLineFollowerRun3(-65)
    print("after line follower")
    gradualGyroBackward(30, 100)
    # Turns
    #robot.turn(106)
    turnGradualGyro(-90)
    gradualGyroForward(50, 100)

    aMotor.run_angle(10000, 15000)
    gradualGyroBackward(15, 100)

    aMotor.run_angle(10000, -5000)

Run3()