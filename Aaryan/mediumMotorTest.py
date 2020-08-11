#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



# This is where we define the sensors and motors.
ev3 = EV3Brick()
cMotor = Motor(Port.C)
dMotor = Motor(Port.D)
aMotor = Motor(Port.A)
bMotor = Motor(Port.B)
gyro = GyroSensor(Port.S4)
frontColorSensor = ColorSensor(Port.S3)
backColorSensor = ColorSensor(Port.S2)
robot = DriveBase(cMotor, dMotor, 56, 60)

def mediumMotorTest():
    aMotor run_time(100, 2)
    bMotor run_time(100, 2)

