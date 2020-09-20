#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialize the motors.
dMotor = Motor(Port.D)
cMotor = Motor(Port.C)
 

# Initialize the color sensor.
frontColorSensor = ColorSensor(Port.S3)


# Initialize the drive base.
robot = DriveBase(cMotor, dMotor, 56, 60)
# Calculate the light threshold. Choose values based on your measurements.
def lineFollower2():
    f = open("ConfiguredColor.txt","r")
    global frontColorSensorWhite
    global frontColorSensorBlack
    frontColorSensorWhite = int(f.readline())
    frontColorSensorBlack = int(f.readline())


    threshold = (frontColorSensorWhite + frontColorSensorBlack) / 2

    # Set the drive speed at 100 millimeters per second.
    DRIVE_SPEED = 100

    # Set the gain of the proportional line controller. This means that for every
    # percentage point of light deviating from the threshold, we set the turn
    # rate of the drivebase to 1.2 degrees per second.

    # For example, if the light value deviates from the threshold by 10, the robot
    # steers at 10*1.2 = 12 degrees per second.
    PROPORTIONAL_GAIN = 1.2

    # Start following the line endlessly.
    while True:

        # Calculate the deviation from the threshold.
        deviation = line_sensor.reflection() - threshold

        # Calculate the turn rate.
        turn_rate = PROPORTIONAL_GAIN * deviation

        # Set the drive base speed and turn rate.
        robot.drive(speed, turn_rate)

        # You can wait for a short time or do other things in this loop.
        wait(10)