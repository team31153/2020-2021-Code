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
    gradualGyroForward(119, 200)
    turnGradualGyro(37)
    robot.straight(212)
    t1 = Thread(target=aMotor.run_angle, args=([8000, 2700]))
    t1.start()
    bMotor.run_angle(1560, -7000)
    robot.straight(-70)
    turnGradualGyro(11)
    robot.straight(-110)
    wait(30)
    aMotor.run_angle(8000, -2700)
    robot.turn(35)
    robot.straight(-1600)

Run1()