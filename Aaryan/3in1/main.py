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
t_end = time.time() + 2
blackValueBack = -1
blackValueFront = -1
whiteValueBack = -1
whiteValueFront = -1
desiredDistance =  100
speed = 75

# The Function
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

def stopOnWBFront():
    f = open("blackValueBack.txt","r")
    global blackValueBack
    global blackValueFront
    global whiteValueBack
    global whiteValueFront
    blackValueBack = int(f.readline())
    blackValueFront = int(f.readline())
    whiteValueBack = int(f.readline())
    whiteValueFront = int(f.readline())
    
    
    # Create your objects here
    # Initialize the EV3 Brick.
    ev3 = EV3Brick()
    # Initialize a motor at port B.
    frontColorSensor = ColorSensor(Port.S3)
    cMotor = Motor(Port.C)
    dMotor = Motor(Port.D)
    robot = DriveBase(cMotor, dMotor, 56, 60)
    # Write your program here
    # Play a sound.
    ev3.speaker.beep()
    # Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
    while True:
        if (frontColorSensor.reflection() >= whiteValueFront):
            ev3.speaker.beep()
            robot.stop()
            break 
        else:
            robot.drive(30,0)
    while True:
        if (frontColorSensor.reflection() <= blackValueFront):
            ev3.speaker.beep()
            robot.stop()
            break
        else:
            robot.drive(30,0)
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

config()
stopOnWBFront()
gradualGyroForward(desiredDistance, speed)

