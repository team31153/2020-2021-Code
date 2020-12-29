#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
from threading import Thread

# Create your objects here.
ev3 = EV3Brick()

#Initialize Motors
aMotor = Motor(Port.A)
bMotor = Motor(Port.B)
cMotor = Motor(Port.C)
dMotor = Motor(Port.D)
robot = DriveBase(cMotor, dMotor, 56, 60)

#initialize color sensors
p1BSensor = ColorSensor(Port.S1)
p2SSensor = ColorSensor(Port.S2)
p3FSensor = ColorSensor(Port.S3)
p4GSensor = GyroSensor(Port.S4)

# Global color sensor values
frontColorSensorWhite = -1
backColorSensorWhite = -1
sideColorSensorWhite = -1
frontColorSensorBlack = -1
backColorSensorBlack = -1
sideColorSensorBlack = -1
