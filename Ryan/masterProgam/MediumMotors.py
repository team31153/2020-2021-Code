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
def mediumMotors():
    ev3 = EV3Brick()
    aMotor = Motor(Port.A)
    bMotor = Motor(Port.B)

    # Write your program here.
    while True:
        listOfButtons = ev3.buttons.pressed()
        for oneButton in listOfButtons:
            print(oneButton)
            if oneButton == Button.RIGHT:
                aMotor.run_target(200, 180)
                print("Angle of horizontal motor is " + str(aMotor.angle()))
                aMotor.reset_angle(0)
            if oneButton == Button.LEFT:
                aMotor.run_target(200, -180)
                print("Angle of horizontal motor is " + str(aMotor.angle()))
                aMotor.reset_angle(0)
            if oneButton == Button.UP:
                bMotor.run_target(200, 180)
                print("Angle of vertical motor is " + str(bMotor.angle()))
                bMotor.reset_angle(0)
            if oneButton == Button.DOWN:
                bMotor.run_target(200, -180)
                print("Angle of vertical motor is " + str(bMotor.angle()))
                bMotor.reset_angle(0)
    
    

