#!/usr/bin/env pybricks-micropython
# Aaryan and Felix code here.
from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *
from GyroB import *
from GyroF import *

# # ORIGINALLY Run1Test
# RYAN CHANGED IT TO Run2Test ON 1/3/20

readAllValues()

# Code Here.
def Run2():
    robot.straight(200)
    gradualGyroForward(200,26)
Run2()