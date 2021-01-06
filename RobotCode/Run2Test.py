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
    t1 = Thread(target=aMotor.run_angle, args=([8000, 1300]))
    t1.start()
    bMotor.run_angle(8000, -7000)
    robot.straight(-70)
    turnGradualGyro(13)
    robot.straight(-110)
    wait(30)
    aMotor.run_angle(8000, -500)
    t2 = Thread(target=aMotor.run_angle, args=([8000, -2200]))
    t2.start()
    robot.turn(41)
    robot.straight(-1600)
Run2()