#!/usr/bin/env pybricks-micropython
from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *
from threading import Thread

readAllValues()

# t1 = Thread(target=gradualGyroForward, args=([65, 40]))
# t1.start()
# aMotor.run_angle(10000, -3000)
gradualGyroBackward(680, 200)
# readAllValues()
# stopOnBlackF()

