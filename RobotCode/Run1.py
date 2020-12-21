#!/usr/bin/env pybricks-micropython
# Aaryan and Felix code here.
from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *
from GyroB import *
from GyroF import *

readAllValues()

# Code Here.
def Run1():
    gradualGyroForward(380, 200)
    sideLineFollowerRun1(80)
    wait(10)
    gyroForward(60, 80)
    gradualGyroForward(200, 26)
    robot.straight(-90)
    robot.turn(110)
    robot.straight(130)
    robot.turn(-80)
    frontLineFollowerStopWithSide(50)
    robot.turn(103)
    robot.straight(100)
    robot.turn(-101)
    stopOnWhiteBForward()
    aMotor.run_angle(7000, 2830)
    gradualGyroForward(300, 75)
    aMotor.run_angle(7000, -200)
    gradualGyroBackward(180, 80)
    aMotor.run_angle(7000, -2630)
    
Run1()