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

def Run3MK2():

    # Get out of base to go on line
    gradualGyroBackward(650, 300)
    # Line follows
    # print("before line follower")
    backLineFollowerRun3(-50)
    gradualGyroBackward(30, 30)
    # print("after line follower")
    # Turns
    #robot.turn(106)
    turnGradualGyro(-82)
    #sideLineFollowerRun3(50)
    gradualGyroBackward(45, 100)

    aMotor.run_angle(1560, -4500)
    t1 = Thread(target=gradualGyroForward, args=([65, 40]))
    t1.start()
    turnGradualGyro(-4)
    aMotor.run_angle(1560, -3000)
    # stopOnBlackS()


    run3Pt2()
    gradualGyroForward(7, 20)
    turnGradualGyro(7)
    bMotor.run_angle(1560, 2800)
    turnGradualGyro(-7)
    gradualGyroBackward(7, 20)

    stopOnBlackF()
    turnGradualGyro(-50)
    gradualGyroBackward(270, 200)

    def dance():
        while True:
            robot.straight(10)
            robot.straight(-10)
    dance()