#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time


from stopOnWhiteBlackFront import stopOnWBFront
from gradualGyroStraight import gradualGyroForward
from stopOn_T_Junction import stopOnT
from configurationColor import config




# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


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
blackValueBack = -1
blackValueFront = -1
whiteValueBack = -1
whiteValueFront = -1

# These are the inputs.

#desiredDistance = int(input("What is the Distance you wanna travel?"))
#speed = int(input("What is the Speed you wanna go at?"))

# This is the main Program

#print("Configuration Done. Place Robot")
#time.sleep(5)
#print("Program starts now")

stopOnT()




