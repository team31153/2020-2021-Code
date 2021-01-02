#!/usr/bin/env pybricks-micropython

from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *
from Run3Pt2 import run3Pt2
from Run3Pt3 import run3Pt3
from threading import Thread

readAllValues()
p4GSensor.reset_angle(0)

def Run3():

    # Get out of base to go on line
    gradualGyroBackward(650, 300)
    # Line follows
    # print("before line follower")
    backLineFollowerRun3(-50)
    gradualGyroBackward(20, 30)
    # print("after line follower")
    # Turns
    #robot.turn(106)
    turnGradualGyro(-84)
    #sideLineFollowerRun3(50)
    gradualGyroBackward(25, 100)

    aMotor.run_angle(1560, -4500)
    t1 = Thread(target=gradualGyroForward, args=([65, 40]))
    t1.start()
    aMotor.run_angle(1560, -3000)
    # stopOnBlackS()


    run3Pt2()
    bMotor.run_angle(1560, 2800)

    readAllValues()
    stopOnBlackF()
    p4GSensor.reset_angle(0)
    turnGradualGyro(40)
    gradualGyroForward(20, 30)
    turnGradualGyro(25)
    gradualGyroBackward(60, 30)
    gradualGyroForward(10, 30)
    turnGradualGyro(-35)
    turnGradualGyro(100)
    gradualGyroForward(400, 200)
    # gradualGyroBackward(25)
    # turnGradualGyro(-30)
    # run3Pt3()

    def dance():
        while True:
            robot.straight(10)
            robot.straight(-10)
            robot.turn(30)
    dance()



Run3()