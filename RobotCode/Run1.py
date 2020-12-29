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
    frontLineFollowerStopWithSide(80)
    robot.turn(103)
    robot.straight(115)
    robot.turn(-101)
    stopOnWhiteBForward()
    robot.straight(20)
    aMotor.run_angle(7000, 2800)
    gradualGyroForward(280, 75)
    gradualGyroBackward(180, 80)
    aMotor.run_angle(7000, -2800)
    robot.straight(-140)
    robot.turn(-90)
    robot.straight(60)
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