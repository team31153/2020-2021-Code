#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
#Calls functions from programs
from TurnGradualGyro import turnGradualGyro
from GradualGyroF import gradualGyroForward
from GradualGyroB import gradualGyroBackward
from ColorSensorFunctions import stopOnBlackF
from ColorSensorFunctions import stopOnBlackB
from ColorSensorFunctions import stopOnBlackS
from ColorSensorFunctions import stopOnWhiteF
from ColorSensorFunctions import stopOnWhiteB
from ColorSensorFunctions import stopOnWhiteS
from ColorSensorFunctions import sideLineFollower
from ColorSensorFunctions import backLineFollowerRun3
from ColorSensorFunctions import backLineFollower
from ColorSensorFunctions import align1Run3



# Create your objects here.
ev3 = EV3Brick()

#Initialize Motors
aMotor = Motor(Port.A)
bMotor = Motor(Port.B)
cMotor = Motor(Port.C)
dMotor = Motor(Port.D)
robot = DriveBase(cMotor, dMotor, 55, 104)

#initialize color sensors
p1BSensor = ColorSensor(Port.S1)
p2SSensor = ColorSensor(Port.S2)
p3FSensor = ColorSensor(Port.S3)
p4GSensor = GyroSensor(Port.S4)

# Write your program here.
#Calls functions imported from programs

# Get out of base to go on line
gradualGyroBackward(200, 100, p4GSensor, cMotor, dMotor, robot)
# Line follows
print("before line follower")
backLineFollowerRun3(p1BSensor, p2SSensor, cMotor, dMotor, robot, -65)
print("after line follower")
gradualGyroBackward(30, 100, p4GSensor, cMotor, dMotor, robot)
# Turns
#robot.turn(106)
turnGradualGyro(-90, cMotor, dMotor, robot, p4GSensor)
gradualGyroForward(50, 100, p4GSensor, cMotor, dMotor, robot)

aMotor.run_angle(10000, 15000)
gradualGyroBackward(15, 100, p4GSensor, cMotor, dMotor, robot)

aMotor.run_angle(10000, -5000)