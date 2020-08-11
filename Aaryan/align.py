#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from stopOnWhiteBlackFront import stopOnWBFront
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

blackValueBack = -1
blackValueFront = -1
whiteValueBack = -1
whiteValueFront = -1

def align():
    global blackValueBack
    global blackValueFront
    global whiteValueBack
    global whiteValueFront
    blackValueBack = int(f.readline())
    blackValueFront = int(f.readline())
    whiteValueBack = int(f.readline())
    whiteValueFront = int(f.readline())

    t_end = time.time() + 2
    distanceTraveled = robot.distance()
    threshold = (50 + 10) / 2
    DRIVE_SPEED = 100
    PROPORTIONAL_GAIN = 1.2

    while time.time() < t_end:

        deviation = frontColorSensor() - threshold

        turn_rate = PROPORTIONAL_GAIN * deviation

        robot.drive(speed, turn_rate)



