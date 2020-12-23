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
    robot.straight(-90)
    robot.turn(110)
    robot.straight(130)
    robot.turn(-80)
    frontLineFollowerStopWithSide(50)
    robot.turn(103)
    robot.straight(90)
    robot.turn(-101)
    stopOnWhiteBForward()
    aMotor.run_angle(7000, 2850)
    gradualGyroForward(290, 75)
    gradualGyroBackward(160, 80)
    aMotor.run_angle(7000, -2850)
    robot.straight(-100)
    robot.turn(-80)
    gyroForward(90,100)
    robot.turn(80)
    frontLineFollowerStopWithSide(30)
    turnGradualGyro(-44)
    gyroForward(110,200)
    turnGradualGyro(44.5)
Run1()