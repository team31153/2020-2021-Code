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
from ConfigurationColorMK2 import colorConfigMK2
from StopOnBlackMK3 import stopOnBlackF
from StopOnBlackMK3 import stopOnBlackB
from StopOnBlackMK3 import stopOnBlackS
from StopOnBlackMK3 import stopOnWhiteF
from StopOnBlackMK3 import stopOnWhiteB
from StopOnBlackMK3 import stopOnWhiteS
from StopOnBlackMK3 import sideLineFollower
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
p4FSensor = GyroSensor(Port.S4)
stop = 0

# Write your program here.
#Calls functions imported from programs

def waiting():
    ev3.screen.clear()
    ev3.screen.draw_text(0, 50, "Choose a")
    ev3.screen.draw_text(0, 70, "program")



while True:

    listOfButtons = ev3.buttons.pressed()
    for oneButton in listOfButtons:
        print(oneButton)
        waiting()
        if oneButton == Button.CENTER:
            colorConfigMK2()
            waiting()
        if oneButton == Button.UP:
            sideLineFollower(p3SSensor)
        if oneButton == Button.RIGHT:
            stopOnBlackF()
        if oneButton == Button.DOWN:
            stopOnBlackB()
        if oneButton == Button.LEFT:
            turnGradualGyro()
