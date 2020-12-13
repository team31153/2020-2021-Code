#!/usr/bin/env pybricks-micropython
from Initialize import *


# Create your objects here.
def turnGradualGyro(i):

    # Write your program here.
    p4GSensor.reset_angle(0)

    # Write your program here.
    #Asks for the angle the user wants the robot to turn
    def GradualGyroTurnC(degrees):
        #Sets variables and measures gyro angle
        p4GSensor.reset_angle(0)
        initialGyro = p4GSensor.angle()
        newAngle = 0
        steering = -70
        speed = 0
        #Make robot keep on turning until it has reached the inputed degrees
        while newAngle < degrees:
            robot.drive(speed, steering)
            speed = speed+0.1
            newAngle = initialGyro + p4GSensor.angle()
        while newAngle > degrees:
            robot.drive(speed, steering)
            newAngle = initialGyro + p4GSensor.angle()
        #Robot stops after reaching inputed degrees
        robot.stop(Stop.COAST)

    def GradualGyroTurnAC(degrees):
        #Sets variables and measures gyro angle
        p4GSensor.reset_angle(0)
        initialGyro = p4GSensor.angle()
        newAngle = 0
        steering = 90
        nsteering = -90
        speed = 5
        #Make robot keep on turning until it has reached the inputed degrees
        while newAngle > degrees:
            robot.drive(speed, steering)
            newAngle = initialGyro + p4GSensor.angle()            
        while newAngle < degrees:
            robot.drive(speed, nsteering)
            newAngle = initialGyro + p4GSensor.angle()
        #Robot stops after reaching inputed degrees
        robot.stop(Stop.COAST)

    if i > 0:
        #if angle is positive then turn clockwise
        GradualGyroTurnC(i)
    elif i < 0:
        #if angle is negative then turn anticlockwise
        GradualGyroTurnAC(i)
    else:
        #if angle is 0 then don't  durn
        print("Invalid Angle")

