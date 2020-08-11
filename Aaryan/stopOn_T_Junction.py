#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from stopOnWhiteBlackFront import stopOnWBFront
from configurationColor import *
from align import align
import time

ev3 = EV3Brick()
cMotor = Motor(Port.C)
dMotor = Motor(Port.D)
aMotor = Motor(Port.A)
bMotor = Motor(Port.B)
gyro = GyroSensor(Port.S4)
frontColorSensor = ColorSensor(Port.S3)
backColorSensor = ColorSensor(Port.S2)
robot = DriveBase(cMotor, dMotor, 56, 60)
t_end = time.time() + 2
blackValueBack = -1
blackValueFront = -1
whiteValueBack = -1
whiteValueFront = -1

# The Program
def stopOnT():
    
    

    f = open("blackValueBack.txt","r")
    global blackValueBack
    global blackValueFront
    global whiteValueBack
    global whiteValueFront
    blackValueBack = int(f.readline())
    blackValueFront = int(f.readline())
    whiteValueBack = int(f.readline())
    whiteValueFront = int(f.readline())

    distanceTraveled = robot.distance()
    DRIVE_SPEED = 100
    PROPORTIONAL_GAIN = 1.8
    threshold = (whiteValueFront + blackValueFront)/2


    while True:
        if (frontColorSensor.reflection() >= (whiteValueFront - 5)):
            ev3.speaker.beep()
            robot.stop()
            break 
        else:
            robot.drive(30,0)
    while True:
        if (frontColorSensor.reflection() <= blackValueFront):
            ev3.speaker.beep()
            robot.stop()
            break
        else:
            robot.drive(30,0)
    robot.turn(75)
    time.sleep(1)
    while True:
        deviation = frontColorSensor.reflection() - threshold

        turn_rate = PROPORTIONAL_GAIN * deviation

        robot.drive(30, -turn_rate)

        if (backColorSensor.reflection() <= blackValueBack):
            robot.stop()
            break
