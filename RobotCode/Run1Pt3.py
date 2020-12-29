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
    frontLineFollowerStopWithSide(50)
    gradualGyroBackward(80, 120)
    turnGradualGyro(-40)
    gradualGyroForward(130,200)
    turnGradualGyro(37)
    robot.straight(214)
    t1 = Thread(target=aMotor.run_angle, args=([8000, 2700]))
    t1.start()
    bMotor.run_angle(14000, -6000)
    
Run1()