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
    frontLineFollowerStopWithSide(45)
    robot.turn(101)
    robot.straight(135)
    robot.turn(-101)
    robot.straight(41)
    aMotor.run_angle(7000, 2750)
    gradualGyroForward(250, 200)
    aMotor.run_angle(7000, -2750)
    
Run1()