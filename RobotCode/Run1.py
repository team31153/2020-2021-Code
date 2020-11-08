#!/usr/bin/env pybricks-micropython
# Aaryan and Felix code here.
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

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
from ColorSensorFunctions import backLineFollower



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
# Create your objects here.
ev3 = EV3Brick()
#initialize color sensors
p1BSensor = ColorSensor(Port.S1)
p2SSensor = ColorSensor(Port.S2)
p3FSensor = ColorSensor(Port.S3)
ev3 = EV3Brick()
cMotor = Motor(Port.C)
dMotor = Motor(Port.D)
aMotor = Motor(Port.A)
bMotor = Motor(Port.B)
gyro = GyroSensor(Port.S4)



robot = DriveBase(cMotor, dMotor, wheel_diameter=56, axle_track=60)
"colorConfig()"

gradualGyroForward(865, 100)
wait(10)
gradualGyroForward(210, 29)
robot.straight(-80)
robot.turn(81)
robot.straight(90)
lineFollower(300)