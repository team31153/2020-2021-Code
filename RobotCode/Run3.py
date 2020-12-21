#!/usr/bin/env pybricks-micropython

from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *
from Run3Pt2 import run3Pt2

readAllValues()
p4GSensor.reset_angle(0)

def Run3():

    # Get out of base to go on line
    gradualGyroBackward(620, 100)
    # Line follows
    # print("before line follower")
    backLineFollowerRun3(-50)
    # print("after line follower")
    # Turns
    #robot.turn(106)
    turnGradualGyro(-84)
    #sideLineFollowerRun3(50)
    gradualGyroBackward(25, 100)

    aMotor.run_angle(10000, -4500)
    gradualGyroForward(65, 20)
    aMotor.run_angle(10000, -3000)

    run3Pt2()
    bMotor.run_angle(1000, 5700)
    bMotor.run_angle(1000, -5700)
    bMotor.run_angle(1000, 5700)
    bMotor.run_angle(1000, -5700)
    bMotor.run_angle(1000, 5700)
    bMotor.run_angle(1000, -5700)


Run3()