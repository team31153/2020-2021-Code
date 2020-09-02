#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
#Calls functions from programs
from TurnGradualGyro import turnGradualGyro
from ConfigurationColor import colorConfig
from StopOnBlackMK3 import stopOnBlackF
from StopOnBlackMK3 import stopOnBlackB
from StopOnBlackMK3 import stopOnBlackS
from StopOnBlackMK3 import stopOnWhiteF
from StopOnBlackMK3 import stopOnWhiteB
from StopOnBlackMK3 import stopOnWhiteS
from StopOnBlackMK3 import test
from GradualStraightF import gradualStraightF
from GradualStraightB import gradualStraightB
from MediumMotors import mediumMotors

# Create your objects here.
ev3 = EV3Brick()

#Initialize Motors
cMotor = Motor(Port.C)
dMotor = Motor(Port.D)
robot = DriveBase(cMotor, dMotor, 56, 60)

#initialize color sensors
p1FSensor = ColorSensor(Port.S1)
p2BSensor = ColorSensor(Port.S2)
p3SSensor = ColorSensor(Port.S3)

# Write your program here.
#Calls functions imported from programs

whichProgram = input("Which program do you want to run? ")
whichProgram = int(whichProgram)

if whichProgram == 1:
    colorConfig()
elif whichProgram == 2:
    stopOnBlackF()
elif whichProgram == 3:
    stopOnBlackB()
elif whichProgram == 4:
    stopOnBlackS()
elif whichProgram == 5:
    stopOnWhiteF()
elif whichProgram == 6:
    stopOnWhiteB()
elif whichProgram == 7:
    stopOnWhiteS()
elif whichProgram == 8:
    turnGradualGyro()
elif whichProgram == 9:
    gradualStraightF()
elif whichProgram == 10:
    gradualStraightB()
elif whichProgram == 11:
    mediumMotors()
else:
    print("Not an option, try again.")
