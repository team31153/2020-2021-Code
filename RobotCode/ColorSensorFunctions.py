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

#Initialize Motors
cMotor = Motor(Port.C)
dMotor = Motor(Port.D)
robot = DriveBase(cMotor, dMotor, 56, 60)

#initialize color sensors
p1BSensor = ColorSensor(Port.S1)
p2SSensor = ColorSensor(Port.S2)
p3FSensor = ColorSensor(Port.S3)

frontColorSensorWhite = -1
backColorSensorWhite = -1
sideColorSensorWhite = -1
frontColorSensorBlack = -1
backColorSensorBlack = -1
sideColorSensorBlack = -1

# Write your program here.
def readAllValues():
    # Read all Files
    f = open("ConfiguredColor.txt", "r")
    global frontColorSensorWhite
    global backColorSensorWhite
    global sideColorSensorWhite
    global frontColorSensorBlack
    global backColorSensorBlack
    global sideColorSensorBlack
    frontColorSensorWhite = int(f.readline())
    backColorSensorWhite = int(f.readline())
    sideColorSensorWhite = int(f.readline())
    frontColorSensorBlack = int(f.readline())
    backColorSensorBlack = int(f.readline())
    sideColorSensorBlack = int(f.readline())
    print("In read all values" + str(frontColorSensorBlack))
    f.close()

def test():
    readAllValues()
    print("in test" + str(frontColorSensorBlack))

def stopOnWhiteF():
    
    readAllValues()
    print("Read configured color front value: " + str(frontColorSensorWhite))

    while p3FSensor.reflection() < frontColorSensorWhite:
        #print(frontColorSensorWhite)
        robot.drive(100,0)
    robot.stop(Stop.BRAKE)

def stopOnWhiteB():

    readAllValues()
    print("Read configured color back value: " + str(backColorSensorWhite))

    while p1BSensor.reflection() < backColorSensorWhite:
        print(backColorSensorWhite)
        robot.drive(-100,0)
    robot.stop(Stop.BRAKE)

def stopOnWhiteS():

    readAllValues()
    print("Read configured color side value: " + str(sideColorSensorWhite))

    while p2SSensor.reflection() < sideColorSensorWhite:
        print(sideColorSensorWhite)
        robot.drive(100,0)
    robot.stop(Stop.BRAKE)

def stopOnBlackF():
    
    readAllValues()
    print("Read configured color front value: " + str(frontColorSensorBlack))

    while p3FSensor.reflection() > frontColorSensorBlack:
        #print(frontColorSensorBlack)
        robot.drive(100,0)
    robot.stop(Stop.BRAKE)

def stopOnBlackB():

    readAllValues()
    print("Read configured color back value: " + str(backColorSensorBlack))

    while p1BSensor.reflection() > backColorSensorBlack:
        print(backColorSensorBlack)
        robot.drive(-100,0)
    robot.stop(Stop.BRAKE)

def stopOnBlackS():

    readAllValues()
    print("Read configured color side value: " + str(sideColorSensorBlack))

    while p2SSensor.reflection() > sideColorSensorBlack:
        print(sideColorSensorBlack)
        robot.drive(100,0)
    robot.stop(Stop.BRAKE)

def sideLineFollower(line_sensor):

    readAllValues()
    print("Read configured color side value white: " + str(sideColorSensorWhite))
    print("Read configured color side value black: " + str(sideColorSensorBlack))

    

    threshold = (sideColorSensorWhite + sideColorSensorBlack) / 2

    # Set the drive speed at 100 millimeters per second.
    speed = 100

    # Set the gain of the proportional line controller. This means that for every
    # percentage point of light deviating from the threshold, we set the turn
    # rate of the drivebase to 1.2 degrees per second.

    # For example, if the light value deviates from the threshold by 10, the robot
    # steers at 10*1.2 = 12 degrees per second.
    PROPORTIONAL_GAIN = -0.7

    # Start following the line endlessly.

    while True:

        # Calculate the deviation from the threshold.
        deviation = line_sensor.reflection() - threshold
        
        # Calculate the turn rate.
        turn_rate = PROPORTIONAL_GAIN * deviation

        print("Color sensor reflection is " + str(line_sensor.reflection()))
        print("Turn rate is: " + str(turn_rate))
        # Set the drive base speed and turn rate.
        robot.drive(speed, turn_rate)

def backLineFollower(line_sensor, desiredDistance):

    readAllValues()
    print("Read configured color back value white: " + str(backColorSensorWhite))
    print("Read configured color back value black: " + str(backColorSensorBlack))

    ev3 = EV3Brick()
    gyro = GyroSensor(Port.S4)
    cMotor = Motor(Port.C)
    dMotor = Motor(Port.D)
    robot = DriveBase(cMotor, dMotor, 56, 60)    

    threshold = (backColorSensorWhite + backColorSensorBlack) / 2

    # Set the drive speed at 100 millimeters per second.
    speed = -100

    robot.reset()

    #Setting the initial value for distance
    distanceTraveled = robot.distance()

    # Set the gain of the proportional line controller. This means that for every
    # percentage point of light deviating from the threshold, we set the turn
    # rate of the drivebase to 1.2 degrees per second.

    # For example, if the light value deviates from the threshold by 10, the robot
    # steers at 10*1.2 = 12 degrees per second.
    PROPORTIONAL_GAIN = 0.8

    # Start following the line endlessly.

    while distanceTraveled > desiredDistance:
        distanceTraveled = robot.distance()

        # Calculate the deviation from the threshold.
        deviation = line_sensor.reflection() - threshold
        
        # Calculate the turn rate.
        turn_rate = PROPORTIONAL_GAIN * deviation

        print("Color sensor reflection is " + str(line_sensor.reflection()))
        print("Turn rate is: " + str(turn_rate))
        # Set the drive base speed and turn rate.
        robot.drive(speed, turn_rate)
