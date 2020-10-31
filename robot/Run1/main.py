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
#initialize color sensors
p1BSensor = ColorSensor(Port.S1)
p2SSensor = ColorSensor(Port.S2)
p3FSensor = ColorSensor(Port.S3)
ev3 = EV3Brick()
cMotor = Motor(Port.C)
dMotor = Motor(Port.D)
aMotor = Motor(Port.A)
bMotor = Motor(Port.B)
gyro = GyroSensor(Port.S4)



robot = DriveBase(cMotor, dMotor, wheel_diameter=56, axle_track=60)

blackValueBack = -1
blackValueFront = -1
whiteValueBack = -1
whiteValueFront = -1
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
def colorConfig():
    readAllValues
    frontWhite = -1000
    sideWhite = -1000
    backWhite = -1000

    while frontWhite == -1000 or sideWhite == -1000 or backWhite == -1000:
        listOfButtons = ev3.buttons.pressed()
        for oneButton in listOfButtons:
            print(oneButton)
            if oneButton == Button.RIGHT:
                sideWhite = p2SSensor.reflection()
                print("Side value is: " + str(sideWhite))
                ev3.screen.clear()
                ev3.screen.draw_text(0, 50, "Side color sensor")
                ev3.screen.draw_text(0, 70, "white: " + str(sideWhite))
            elif oneButton == Button.UP:
                frontWhite = p3FSensor.reflection()
                print("Front value is: " + str(frontWhite))
                ev3.screen.clear()
                ev3.screen.draw_text(0, 50, "Front color sensor")
                ev3.screen.draw_text(0, 70, "white: " + str(frontWhite))
            elif oneButton == Button.DOWN:
                backWhite = p1BSensor.reflection()
                print("Back value is: " + str(backWhite))
                ev3.screen.clear()
                ev3.screen.draw_text(0, 50, "Back color sensor")
                ev3.screen.draw_text(0, 70, "white: " + str(backWhite))

    print("White sensing is done.") 
    ev3.screen.clear()
    ev3.screen.draw_text(0,50, "White sensing")
    ev3.screen.draw_text(0,70, "is done.")
    time.sleep(2)

    print("Starting sensing for black.")
    ev3.screen.clear()
    ev3.screen.draw_text(0,50, "Starting sensing")
    ev3.screen.draw_text(0,70, "for black.")
    frontBlack = 1000
    sideBlack = 1000
    backBlack = 1000

    while frontBlack == 1000 or sideBlack == 1000 or backBlack == 1000:
        listOfButtons = ev3.buttons.pressed()
        for oneButton in listOfButtons:
            print(oneButton)
            if oneButton == Button.RIGHT:
                sideBlack = p2SSensor.reflection()
                print("Side value is: " + str(sideBlack))
                ev3.screen.clear()
                ev3.screen.draw_text(0, 50, "Side color sensor")
                ev3.screen.draw_text(0, 70, "black: " + str(sideBlack))
            elif oneButton == Button.UP:
                frontBlack = p3FSensor.reflection()
                print("Front value is: " + str(frontBlack))
                ev3.screen.clear()
                ev3.screen.draw_text(0, 50, "Front color sensor")
                ev3.screen.draw_text(0, 70, "black: " + str(frontBlack))
            elif oneButton == Button.DOWN:
                backBlack = p1BSensor.reflection()
                print("Back value is: " + str(backBlack))
                ev3.screen.clear()
                ev3.screen.draw_text(0, 50, "Back color sensor")
                ev3.screen.draw_text(0, 70, "black: " + str(backBlack))
    print("Black sensing is done.")
    ev3.screen.clear()
    ev3.screen.draw_text(0,50, "Black sensing")
    ev3.screen.draw_text(0,70, "is done.")
    ev3.screen.draw_text(0,90, "Writing file.")
    print("writing file")
    #Write values to file
    f = open("ConfiguredColor.txt", "w")
    f.write(str(frontWhite)+'\n')
    f.write(str(backWhite)+'\n')
    f.write(str(sideWhite)+'\n')
    f.write(str(frontBlack)+'\n')
    f.write(str(backBlack)+'\n')
    f.write(str(sideBlack)+'\n')
    f.close()
    print("finished writing file")
    ev3.screen.clear()
    ev3.screen.draw_text(0,50, "Finished")
    ev3.screen.draw_text(0,70, "writing file")
def lineFollower(lineFollowingDistance):
    distanceTraveled = robot.distance()


    threshold = (75 + 9) / 2

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
            rampPower = rampPower + 0.5

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
def gradualGyroBackward(desiredDistance, speed):
    print("desiredDistance:" + str(desiredDistance))
    print("Speed:" + str(speed))
    
    initialGyro = 0
    rampPower = 0
    
 

    # Here is the main code.
    robot.reset()

    #Setting the initial value for distance
    distanceTraveled = robot.distance()

    gyro.reset_angle(0) #resets the gyro angle to zero

    while distanceTraveled > desiredDistance: #while the current distance of the robot is less than the distance that we want to go:
        distanceTraveled = robot.distance() #we define the distance traveled variable again, as this is a while loop, and the distance of the robot from its starting point is always changing
        if rampPower > speed: # this is the "gradual" part of our program, where the speed of the robot increases until it reaches the speed that we wanted it to go at.
            rampPower = rampPower - 0.5

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



"colorConfig()"

gradualGyroForward(865, 100)
wait(10)
gradualGyroForward(210, 29)
robot.straight(-80)
robot.turn(81)
robot.straight(90)
lineFollower(300)







