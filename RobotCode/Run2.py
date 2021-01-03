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
def Run2():
    gradualGyroForward(380, 300)
    sideLineFollowerRun1(80) # Line following to just before step counter (line follow for accuracy)
    wait(10)
    gyroForward(60, 100)
    gradualGyroForward(200, 26) # Step counter
    robot.straight(-90)
    robot.turn(110)
    robot.straight(90)
    robot.turn(-80)
    frontLineFollowerStopWithSide(40)
    robot.turn(103)
    robot.straight(115)
    robot.turn(-101)
    stopOnWhiteBForward()
    stopOnBlackBForward()
    aMotor.run_angle(7000, 2800)
    gradualGyroForward(280, 75)
    gradualGyroBackward(180, 80)
    aMotor.run_angle(7000, -2800)
    # align for mission three, treadmill
    robot.straight(-140)
    robot.turn(-90)
    robot.straight(40)
    robot.turn(45)
    frontLineFollowerStopWithSide(80)
    gradualGyroBackward(80, 200)
    turnGradualGyro(-40)
    gradualGyroForward(119, 200)
    turnGradualGyro(37)
    robot.straight(220)
    t1 = Thread(target=aMotor.run_angle, args=([8000, 14000]))
    t1.start()
    bMotor.run_angle(8000, -7000)
    robot.straight(-70)
    turnGradualGyro(11)
    robot.straight(-110)
    wait(30)
    aMotor.run_angle(8000, -2700)
    robot.turn(38)
    robot.straight(-1600)

#Run2()