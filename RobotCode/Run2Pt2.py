#!/usr/bin/env pybricks-micropython
# Aaryan and Felix code here.
from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *
from GyroB import *
from GyroF import *

# ORIGINALLY Run1Pt2
# RYAN CHANGED IT TO Run2Pt2 ON 1/3/20

readAllValues()

# Code Here.
def Run2():
    robot.straight(-90)
    robot.turn(110)
    robot.straight(90)
    robot.turn(-80)
    frontLineFollowerStopWithSide(80)
    robot.turn(103)
    robot.straight(115)
    robot.turn(-101)
    stopOnWhiteBForward()
    stopOnBlackBForward()
    aMotor.run_angle(7000, 2800)
    gradualGyroForward(280, 75)
    gradualGyroBackward(180, 80)
    aMotor.run_angle(7000, -2800)
    robot.turn(-90)
    robot.straight(60)
    frontLineFollowerStopWithSide(50)
Run2()