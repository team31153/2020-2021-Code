#!/usr/bin/env pybricks-micropython

from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *
from Run3Pt2 import run3Pt2
from Run3Pt3 import run3Pt3
from threading import Thread

# readAllValues()
# p4GSensor.reset_angle(0)

def Run3MK3():
    gradualGyroBackward(950, 600)
    bMotor.run_angle(1560, 2800)
    gradualGyroForward(45, 80)
    turnGradualGyro(-80)
    gradualGyroBackward(55, 80)

    def dance():
        while True:
            robot.straight(10)
            robot.straight(-10)
    dance()