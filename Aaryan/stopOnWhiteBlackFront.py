#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

blackValueBack = -1
blackValueFront = -1
whiteValueBack = -1
whiteValueFront = -1

def stopOnWBFront(whiteValue, blackValue):
    global blackValueBack
    global blackValueFront
    global whiteValueBack
    global whiteValueFront
    blackValueBack = int(f.readline())
    blackValueFront = int(f.readline())
    whiteValueBack = int(f.readline())
    whiteValueFront = int(f.readline())
    
    
    # Create your objects here
    # Initialize the EV3 Brick.
    ev3 = EV3Brick()
    # Initialize a motor at port B.
    frontColorSensor = ColorSensor(Port.S3)
    cMotor = Motor(Port.C)
    dMotor = Motor(Port.D)
    robot = DriveBase(cMotor, dMotor, 56, 60)
    # Write your program here
    # Play a sound.
    ev3.speaker.beep()
    # Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
    while True:
        if (frontColorSensor.reflection() >= whiteValueFront):
            ev3.speaker.beep()
            robot.stop()
            break 
        else:
            robot.drive(30,0)
    while True:
        if (frontColorSensor.reflection() <= blackValueFront):
            ev3.speaker.beep()
            robot.stop()
            break
        else:
            robot.drive(30,0)


