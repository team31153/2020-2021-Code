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


# Create your objects here.
ev3 = EV3Brick()


#Initialize motors
cMotor = Motor(Port.C)
dMotor = Motor(Port.D)
rr = DriveBase(cMotor, dMotor, 56, 60)

# Intialize sensors 
p4FSensor = GyroSensor(Port.S4)
p4FSensor.reset_angle(0)

# Write your program here.
#Asks for the angle the user wants the robot to turn
i = -90

def GradualGyroTurnC(robot, degrees):

    initialGyro = p4FSensor.angle()
    newAngle = 0
    steering = 100
    speed = 0
    while newAngle < degrees:
        robot.drive(speed, steering)
        speed = speed+0.1
        newAngle = initialGyro + p4FSensor.angle()
        print("Angle is " + str(newAngle))
        print("Speed is " + str(speed))
    robot.stop(Stop.COAST)

def GradualGyroTurnAC(robot, degrees):

    initialGyro = p4FSensor.angle()
    newAngle = 0
    steering = -100
    speed = 0
    while newAngle > degrees:
        robot.drive(speed, steering)
        speed = speed+0.1
        newAngle = initialGyro + p4FSensor.angle()
        print("Angle is " + str(newAngle))
        print("Speed is " + str(speed))
    robot.stop(Stop.COAST)

if i > 0:
    #if angle is positive then turn clockwise
    GradualGyroTurnC(rr, i)
elif i < 0:
    #if angle is negative then turn anticlockwise
    GradualGyroTurnAC(rr, i)
else:
    print("Invalid Angle")

