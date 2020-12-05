#!/usr/bin/env pybricks-micropython
# Aaryan and Felix code here.
from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *
from GyroB import *
from GyroF import *

# Code Here.
def Run1():

    gyroForward(823, 135)
    wait(10)
    gradualGyroForward(200, 25)
    robot.straight(-90)
    robot.turn(90)
    robot.straight(100)
    robot.turn(-80)
    frontLineFollowerStopWithSide(65)
    robot.straight(20)
    frontLineFollowerStopWithSide(65)
    robot.straight(-60)
    robot.turn(110)
    robot.straight(128)
    robot.turn(-100.5)
    gyroForward(200, 100)
    gyroBackward(-75, -100)
    gyroForward(100, 100)
    gyroBackward(-75, -100)
    gyroForward(100, 100)
    gyroBackward(-75, -100)
    gyroForward(100, 100)

Run1()