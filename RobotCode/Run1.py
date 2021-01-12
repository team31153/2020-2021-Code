#!/usr/bin/env pybricks-micropython
# Aaditya and Ishaan code here.
from ColorSensorFunctions import *
from GradualGyroB import *
from GradualGyroF import *
from TurnGradualGyro import *

# ORIGINALLY RUN 2 
# RYAN CHANGED IT TO RUN 1 ON 1/3/20

# readAllValues()
def Run1():
    gradualGyroBackward(200, 150)
    turnGradualGyro(12)
    gradualGyroBackward(115,90)
    turnGradualGyro(-12)
    turnGradualGyro(12)
    robot.stop(Stop.COAST)
    gradualGyroForward(20, 100)
    turnGradualGyro(-1)
    gradualGyroBackward(110, 60)
    gradualGyroForward(270, 200)
    turnGradualGyro(43)
    gradualGyroBackward(570, 200)
    #turnGradualGyro(13)
    #gradualGyroForward(110, 200)
    turnGradualGyro(-66)
    #sideLineFollowerRun2(50)
    t1 = Thread(target=gradualGyroBackward, args=([230, 200]))
    t1.start()
    aMotor.run_angle(1000, 4600)
    gradualGyroForward(50, 100)
    turnGradualGyro(-34)
    gradualGyroBackward(65, 60)
    aMotor.run_angle(1000, -9000)
    gradualGyroForward(60, 90)
    turnGradualGyro(-31)
    gradualGyroForward(300, 200)
    turnGradualGyro(-35)
    gradualGyroBackward(50, 100)



#Run1()