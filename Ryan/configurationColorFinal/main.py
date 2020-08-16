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


# Create your objects here.
ev3 = EV3Brick()
#initialize color sensors
p1FSensor = ColorSensor(Port.S1)
p2BSensor = ColorSensor(Port.S2)
p3SSensor = ColorSensor(Port.S3)

breakLoop1 = 0
breakLoop2 = 0
breakLoop3 = 0
breakLoop4 = 0
breakLoop5 = 0
breakLoop6 = 0

# Write your program here.

#White values
#Front white value
while True:
    listOfButtons1 = ev3.buttons.pressed()
    for oneButton1 in listOfButtons1:
        #checks which buton is prsessed and what to do
        if oneButton1 == Button.UP:
            frontColorSensorWhite = p1FSensor.reflection()
            print("Front white is " + str(frontColorSensorWhite))
            breakLoop1 = 1
            break
    if breakLoop1 == 1:
        break
#Side white value
time.sleep(2)
while True:
    listOfButtons2 = ev3.buttons.pressed()
    for oneButton2 in listOfButtons2:
        #checks which buton is pressed and what to do
        if oneButton2 == Button.UP:
            sideColorSensorWhite = p3SSensor.reflection()
            print("Side white is " + str(sideColorSensorWhite))
            breakLoop2 = 1
            break
    if breakLoop2 == 1:
        break
#Back white value
time.sleep(2)
while True:
    listOfButtons3 = ev3.buttons.pressed()
    for oneButton3 in listOfButtons3:
        #checks which buton is pressed and what to do
        if oneButton3 == Button.UP:
            backColorSensorWhite = p2BSensor.reflection()
            print("Back white is " + str(backColorSensorWhite))
            breakLoop3 = 1
            break
    if breakLoop3 == 1:
        break

#Black values
#Front black value
time.sleep(2)
while True:
    listOfButtons4 = ev3.buttons.pressed()
    for oneButton4 in listOfButtons4:
        #checks which buton is pressed and what to do
        if oneButton4 == Button.UP:
            frontColorSensorBlack = p1FSensor.reflection()
            print("Front black is " + str(frontColorSensorBlack))
            breakLoop4 = 1
            break
    if breakLoop4 == 1:
        break
#Side black value
time.sleep(2)
while True:
    listOfButtons4 = ev3.buttons.pressed()
    for oneButton5 in listOfButtons4:
        #checks which buton is pressed and what to do
        if oneButton5 == Button.UP:
            sideColorSensorBlack = p3SSensor.reflection()
            print("Side black is " + str(sideColorSensorBlack))
            breakLoop5 = 1
            break
    if breakLoop5 == 1:
        break
#Back black value
time.sleep(2)
while True:
    listOfButtons6 = ev3.buttons.pressed()
    for oneButton6 in listOfButtons6:
        #checks which buton is pressed and what to do
        if oneButton6 == Button.UP:
            backColorSensorBlack = p2BSensor.reflection()
            print("Back black is " + str(backColorSensorBlack))
            breakLoop6 = 1
            break
    if breakLoop6 == 1:
        break