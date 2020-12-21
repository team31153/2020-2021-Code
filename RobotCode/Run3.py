#!/usr/bin/env pybricks-micropython

from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *
from Run3Pt2 import run3Pt2

readAllValues()

def Run3():

    # Get out of base to go on line
    gradualGyroBackward(620, 100)
    # Line follows
    # print("before line follower")
    backLineFollowerRun3(-50)
    # print("after line follower")
    gradualGyroBackward(20, 100)
    # Turns
    #robot.turn(106)
    turnGradualGyro(-87)
    sideLineFollowerRun3(50)
    # gradualGyroBackward(25, 100)

    aMotor.run_angle(10000, -4500)
    gradualGyroForward(65, 20)
    aMotor.run_angle(10000, -2600)

    run3Pt2()
    bMotor.run_angle(1000, 5700)
    bMotor.run_angle(1000, -5700)
    bMotor.run_angle(1000, 5700)
    bMotor.run_angle(1000, -5700)
    bMotor.run_angle(1000, 5700)
    bMotor.run_angle(1000, -5700)


Run3()