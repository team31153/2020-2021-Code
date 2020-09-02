#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


def gradualStraightF():
    ev3 = EV3Brick()

    # Write your program here.
    #Initialize motors
    cMotor = Motor(Port.C)
    dMotor = Motor(Port.D)
    robot = DriveBase(cMotor, dMotor, 56, 60)
    # Intialize sensors 
    p1FSensor = ColorSensor(Port.S1)
    p2BSensor = ColorSensor(Port.S2)
    p3SSensor = ColorSensor(Port.S3)
    p4FSensor = GyroSensor(Port.S4)
    
    desiredDistance = input("What is the distance you want to travel? ")
    desiredDistance = int(desiredDistance)
    
    robot.reset()
    speed = 0
    distanceTraveled = 0
    distanceTraveled = robot.distance()

    while distanceTraveled < desiredDistance:
        robot.drive(speed, 0)
        speed = speed+0.4
        distanceTraveled = robot.distance()
        print("Speed of robot is ")
        print(speed)
        print("Distance traveled is ")
        print(robot.distance())
    robot.stop(Stop.COAST)