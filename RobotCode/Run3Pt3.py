#!/usr/bin/env pybricks-micropython

from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *

# readAllValues()

def run3Pt3():
    p4GSensor.reset_angle(0)
    turnSideRun3()
    backLineFollowerRun3(-50)
    #turnSideRun3()

# run3Pt3()