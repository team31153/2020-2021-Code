#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from configurationColor import config

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
cMotor = Motor(Port.C)
dMotor = Motor(Port.D)
aMotor = Motor(Port.A)
bMotor = Motor(Port.B)
gyro = GyroSensor(Port.S4)
frontColorSensor = ColorSensor(Port.S3)
sideColorSensor = ColorSensor(Port.S2)

robot = DriveBase(cMotor, dMotor, wheel_diameter=56, axle_track=60)

blackValueBack = -1
blackValueFront = -1
whiteValueBack = -1
whiteValueFront = -1


# Write your program here.
ev3.speaker.beep()
def sideLineFollower():
    f = open("blackValueBack.txt","r")
    global blackValueBack
    global blackValueFront
    global whiteValueBack
    global whiteValueFront
    blackValueBack = int(f.readline())
    blackValueFront = int(f.readline())
    whiteValueBack = int(f.readline())
    whiteValueFront = int(f.readline())
    threshold = (blackValueBack + whiteValueBack) / 2
    while True:
        proportionalGain = -1.5
        deviation = sideColorSensor.reflection() - threshold
        turnRate = proportionalGain * deviation
        robot.drive(50, turnRate)

config()
sideLineFollower()