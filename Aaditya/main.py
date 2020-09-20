#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from configuration import config
from linefollower import lineFollower2

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
cMotor = Motor(Port.C)
dMotor = Motor(Port.D)
frontColorSensor = ColorSensor(Port.S3)

robot = DriveBase(cMotor, dMotor, wheel_diameter=56, axle_track=60)

frontColorSensorWhite = -1
frontColorSensorBlack = -1

#Write Your Program Here
ev3.speaker.beep()
def sideLine():
    config()
    lineFollower2()

sideLine()