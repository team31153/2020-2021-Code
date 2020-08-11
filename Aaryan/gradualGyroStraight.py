#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# Everything above allows us to import the EV3 files to write our code.
# Click "Open user guide" on the EV3 extension tab for more information.




def gradualGyroForward(desiredDistance, speed):
    print("desiredDistance:" + str(desiredDistance))
    print("Speed:" + str(speed))
    
    initialGyro = 0
    rampPower = 0
    # This is where the variables are defined.
    ev3 = EV3Brick()
    gyro = GyroSensor(Port.S4)
    cMotor = Motor(Port.C)
    dMotor = Motor(Port.D)
    robot = DriveBase(cMotor, dMotor, 56, 60)

    # Here is the main code.
    robot.reset()

    #Setting the initial value for distance
    distanceTraveled = robot.distance()

    gyro.reset_angle(0) #resets the gyro angle to zero

    while distanceTraveled < desiredDistance: #while the current distance of the robot is less than the distance that we want to go:
        distanceTraveled = robot.distance() #we define the distance traveled variable again, as this is a while loop, and the distance of the robot from its starting point is always changing
        if rampPower < speed: # this is the "gradual" part of our program, where the speed of the robot increases until it reaches the speed that we wanted it to go at.
            rampPower = rampPower + 0.3

        # This is the Gyro Part of our code.
        ang = gyro.angle()

        # If the angle that the gyro is sensing is NOT equal to the initial gyro (0)
        if ang != initialGyro:
        # Turn that angle to GET to the value of the initial gyro.
            robot.turn(ang)

        # Print values for debug
        print("RampPower:" + str(rampPower))
        print("Angle:" + str(ang))
        print("Distance:" + str(distanceTraveled))

        # Drive the robot
        robot.drive(rampPower, 0)
    