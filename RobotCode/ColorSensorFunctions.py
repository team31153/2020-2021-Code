#!/usr/bin/env pybricks-micropython
from Initialize import *

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
    # readAllValues()
    print("in test" + str(frontColorSensorBlack))

def stopOnWhiteF():
    
    # readAllValues()
    print("Read configured color front value: " + str(frontColorSensorWhite))

    while p3FSensor.reflection() < frontColorSensorWhite:
        #print(frontColorSensorWhite)
        robot.drive(100,0)
    robot.stop(Stop.BRAKE)

def stopOnWhiteB():

    # readAllValues()
    print("Read configured color back value: " + str(backColorSensorWhite))

    while p1BSensor.reflection() < backColorSensorWhite:
        print(backColorSensorWhite)
        robot.drive(-100,0)
    robot.stop(Stop.BRAKE)

def stopOnWhiteS():

    # readAllValues()
    print("Read configured color side value: " + str(sideColorSensorWhite))

    while p2SSensor.reflection() < sideColorSensorWhite:
        print(sideColorSensorWhite)
        robot.drive(100,0)
    robot.stop(Stop.BRAKE)

def stopOnBlackF():
    
    # readAllValues()
    print("Read configured color front value: " + str(frontColorSensorBlack))

    while p3FSensor.reflection() > frontColorSensorBlack:
        #print(frontColorSensorBlack)
        robot.drive(100,0)
    robot.stop(Stop.BRAKE)

def stopOnBlackB():

    # readAllValues()
    print("Read configured color back value: " + str(backColorSensorBlack))

    while p1BSensor.reflection() > backColorSensorBlack:
        print(backColorSensorBlack)
        robot.drive(-100,0)
    robot.stop(Stop.BRAKE)

def stopOnBlackS():

    # readAllValues()
    print("Read configured color side value: " + str(sideColorSensorBlack))

    while p2SSensor.reflection() > sideColorSensorBlack:
        print(sideColorSensorBlack)
        robot.drive(100,0)
    robot.stop(Stop.BRAKE)

def sideLineFollower():

    # readAllValues()
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
    PROPORTIONAL_GAIN = -0.9

    # Start following the line endlessly.

    while True:

        # Calculate the deviation from the threshold.
        deviation = p2SSensor.reflection() - threshold
        
        # Calculate the turn rate.
        turn_rate = PROPORTIONAL_GAIN * deviation

        print("Color sensor reflection is " + str(p2SSensor.reflection()))
        print("Turn rate is: " + str(turn_rate))
        # Set the drive base speed and turn rate.
        robot.drive(speed, turn_rate)

def backLineFollower(desiredDistance):

    # readAllValues()
    print("Read configured color back value white: " + str(backColorSensorWhite))
    print("Read configured color back value black: " + str(backColorSensorBlack))


    threshold = (backColorSensorWhite + backColorSensorBlack) / 2

    # Set the drive speed at 100 millimeters per second.
    speed = -100

    robot.reset()

    #Setting the initial value for distance
    distanceTraveled = robot.distance()
    print(distanceTraveled)

    # Set the gain of the proportional line controller. This means that for every
    # percentage point of light deviating from the threshold, we set the turn
    # rate of the drivebase to 1.2 degrees per second.

    # For example, if the light value deviates from the threshold by 10, the robot
    # steers at 10*1.2 = 12 degrees per second.
    PROPORTIONAL_GAIN = -0.9

    # Start following the line endlessly.

    while distanceTraveled > desiredDistance:
        distanceTraveled = robot.distance()
        print(distanceTraveled)
        # Calculate the deviation from the threshold.
        deviation = p1BSensor.reflection() - threshold
        
        # Calculate the turn rate.
        turn_rate = PROPORTIONAL_GAIN * deviation

        print("Color sensor reflection is " + str(p1BSensor.reflection()))
        print("Turn rate is: " + str(turn_rate))
        # Set the drive base speed and turn rate.
        robot.drive(speed, turn_rate)

def backLineFollowerRun3(speed):
    # readAllValues()
    print("Read configured color back value white: " + str(backColorSensorWhite))
    print("Read configured color back value black: " + str(backColorSensorBlack))
    print("Read configured color side value black: " + str(sideColorSensorBlack))


    threshold = (backColorSensorWhite + backColorSensorBlack) / 2

    # Set the drive speed at 100 millimeters per second.

    reflection = p2SSensor.reflection()
    sideBlack = sideColorSensorBlack + 2


    # Set the gain of the proportional line controller. This means that for every
    # percentage point of light deviating from the threshold, we set the turn
    # rate of the drivebase to 1.2 degrees per second.

    # For example, if the light value deviates from the threshold by 10, the robot
    # steers at 10*1.2 = 12 degrees per second.
    PROPORTIONAL_GAIN = -1.2

    # Start following the line endlessly.

    while reflection > sideBlack:
        
        reflection = p2SSensor.reflection()
        print(reflection)
        # Calculate the deviation from the threshold.
        deviation = p1BSensor.reflection() - threshold
        
        # Calculate the turn rate.
        turn_rate = PROPORTIONAL_GAIN * deviation

        # Set the drive base speed and turn rate.
        robot.drive(speed, turn_rate)

def align1Run3():
    # readAllValues()
    print("Read configured color back value black: " + str(backColorSensorBlack))
    print("Read configured color front value black: " + str(frontColorSensorBlack))

    frontBlack = frontColorSensorBlack + 3
    backBlack = backColorSensorBlack + 3

    reflection = p3FSensor.reflection()
    speed = 100
    steering = 60

    while reflection > frontBlack:
        robot.turn(steering)
        reflection = p3FSensor.reflection()
        print("Reflection is: " + str(reflection))



def frontLineFollowerStopWithSide(speed):
    # readAllValues()
    print("Read configured color front value white: " + str(frontColorSensorWhite))
    print("Read configured color front value black: " + str(frontColorSensorBlack))

    

    threshold = (frontColorSensorWhite + frontColorSensorBlack) / 2

    # Set the drive speed at 100 millimeters per second.

    # Set the gain of the proportional line controller. This means that for every
    # percentage point of light deviating from the threshold, we set the turn
    # rate of the drivebase to 1.2 degrees per second.

    # For example, if the light value deviates from the threshold by 10, the robot
    # steers at 10*1.2 = 12 degrees per second.
    PROPORTIONAL_GAIN = -1.8
    while p2SSensor.reflection() > sideColorSensorBlack:    
        
    
        # Calculate the deviation from the threshold.
        deviation = p3FSensor.reflection() - threshold
        
        # Calculate the turn rate.
        turn_rate = PROPORTIONAL_GAIN * deviation

        print("Color sensor reflection is " + str(p3FSensor.reflection()))
        print("Turn rate is: " + str(turn_rate))
        # Set the drive base speed and turn rate.
        robot.drive(speed, turn_rate)
    robot.stop

