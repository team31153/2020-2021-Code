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
def turnGradualGyro():
    ev3 = EV3Brick()


    # Write your program here.
    #Initialize motors
    cMotor = Motor(Port.C)
    dMotor = Motor(Port.D)
    rr = DriveBase(cMotor, dMotor, 56, 60)

    # Intialize sensors 
    p4GSensor = GyroSensor(Port.S4)
    p4GSensor.reset_angle(0)

    # Write your program here.
    #Asks for the angle the user wants the robot to turn
    i = 90
    def GradualGyroTurnC(robot, degrees):
        #Sets variables and measures gyro angle
        initialGyro = p4GSensor.angle()
        newAngle = 0
        steering = -100
        speed = 0
        #Make robot keep on turning until it has reached the inputed degrees
        while newAngle < degrees:
            robot.drive(speed, steering)
            speed = speed+0.1
            newAngle = initialGyro + p4GSensor.angle()
            print("Angle is " + str(newAngle))
            print("Speed is " + str(speed))
        #Robot stops after reaching inputed degrees
        robot.stop(Stop.COAST)

    def GradualGyroTurnAC(robot, degrees):
        #Sets variables and measures gyro angle
        initialGyro = p4GSensor.angle()
        newAngle = 0
        steering = 100
        speed = 0
        #Make robot keep on turning until it has reached the inputed degrees
        while newAngle > degrees:
            robot.drive(speed, steering)
            speed = speed+0.1
            newAngle = initialGyro + p4GSensor.angle()
            print("Angle is " + str(newAngle))
            print("Speed is " + str(speed))
        #Robot stops after reaching inputed degrees
        robot.stop(Stop.COAST)

    if i > 0:
        #if angle is positive then turn clockwise
        GradualGyroTurnC(rr, i)
    elif i < 0:
        #if angle is negative then turn anticlockwise
        GradualGyroTurnAC(rr, i)
    else:
        #if angle is 0 then don't  durn
        print("Invalid Angle")
