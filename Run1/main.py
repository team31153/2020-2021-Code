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
cMotor = Motor(Port.C)
dMotor = Motor(Port.D)
aMotor = Motor(Port.A)
bMotor = Motor(Port.B)
gyro = GyroSensor(Port.S4)
frontColorSensor = ColorSensor(Port.S3)
backColorSensor = ColorSensor(Port.S2)
robot = DriveBase(cMotor, dMotor, 56, 60)


# Write your program here.
ev3.speaker.beep()
def config():
    times = 0
    times2 = 0
    while times < 41:
        
        listOfButtons = ev3.buttons.pressed()
        for oneButton in listOfButtons:
            if oneButton == Button.UP:
                whiteValueFront = frontColorSensor.reflection()
                print("Front White Value" + str(whiteValueFront))
                    
            if oneButton == Button.DOWN:
                whiteValueBack = backColorSensor.reflection()
                print("Back White Value" + str(whiteValueBack))
            
        times = times + 0.001

    time.sleep(2)
    ev3.speaker.beep()

    while times2 < 41:
        listOfButtons = ev3.buttons.pressed()
        for oneButton in listOfButtons:
            if oneButton == Button.UP:
                blackValueFront = frontColorSensor.reflection()
                print("Front Black Value" + str(blackValueFront))

            if oneButton == Button.DOWN:
                blackValueBack = backColorSensor.reflection()
                print("Back Black Value" + str(blackValueBack))
    
        times2 = times2 + 0.001
    ev3.speaker.beep()

    f = open("blackValueBack.txt","w")
    f.write(str(blackValueBack)+'\n')
    f.write(str(blackValueFront)+'\n')
    f.write(str(whiteValueBack)+'\n')
    f.write(str(whiteValueFront)+'\n')
    f.close()
def lineFollower(whiteValue, blackValue, lineFollowingDistance):
    distanceTraveled = robot.distance()


    threshold = (whiteValue + blackValue) / 2

    # Set the drive speed at 100 millimeters per second.
    DRIVE_SPEED = 100

    # Set the gain of the proportional line controller. This means that for every
    # percentage point of light deviating from the threshold, we set the turn
    # rate of the drivebase to 1.2 degrees per second.

    # For example, if the light value deviates from the threshold by 10, the robot
    # steers at 10*1.2 = 12 degrees per second.
    PROPORTIONAL_GAIN = 1.2

    # Start following the line endlessly.
    while lineFollowingDistance < distanceTraveled:

        # Calculate the deviation from the threshold.
        deviation = line_sensor.reflection() - threshold

        # Calculate the turn rate.
        turn_rate = PROPORTIONAL_GAIN * deviation

        # Set the drive base speed and turn rate.
        robot.drive(speed, turn_rate)

        # You can wait for a short time or do other things in this loop.
        wait(10)
def gradualGyroForward(desiredDistance, speed):
    print("desiredDistance:" + str(desiredDistance))
    print("Speed:" + str(speed))
    
    initialGyro = 0
    rampPower = 0
    
 

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

gradualGyroForward(845, 100)
wait(10)
gradualGyroForward(20, 100)
wait(10)
gradualGyroForward(20, 100)
wait(10)
gradualGyroForward(20, 100)
wait(10)
gradualGyroForward(20, 100)
wait(10)
gradualGyroForward(20, 100)
wait(10)
gradualGyroForward(20, 100)
wait(10)
gradualGyroForward(20, 100)
wait(10)
gradualGyroForward(20, 100)
wait(10)
gradualGyroForward(20, 100)
wait(10)
gradualGyroForward(10, 100)
wait(10)
robot.straight(-80)
robot.turn(55)
robot.straight(60)







