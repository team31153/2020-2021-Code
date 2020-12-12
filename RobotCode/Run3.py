#!/usr/bin/env pybricks-micropython

from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *

readAllValues()

def Run3():

    # Get out of base to go on line
    gradualGyroBackward(630, 100)
    # Line follows
    # print("before line follower")
    backLineFollowerRun3(-65)
    # print("after line follower")
    gradualGyroBackward(30, 100)
    # Turns
    #robot.turn(106)
    turnGradualGyro(-85)
    gradualGyroForward(50, 100)

    aMotor.run_angle(10000, 7100)
    gradualGyroBackward(95, 100)

    aMotor.run_angle(10000, -5500)
    gradualGyroForward(150, 20)

Run3()