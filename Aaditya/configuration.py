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
p1SSensor = ColorSensor(Port.S3)


# Write your program here.
def config():
    times = 0
    print("white has started")
    #How long the user has to configure for white
    while times < 41:
        #Check if buttons are pressed
        listOfButtons = ev3.buttons.pressed()
        for oneButton in listOfButtons:
            #checks which buton is pressed and what to do
            if oneButton == Button.UP:
                frontColorSensorWhite = p1FSensor.reflection()
                print("Front is " + str(frontColorSensorWhite))


        times = times+0.001
    print("white has reached")
    time.sleep(2)
    print("black has started")
    times2 = 0
    #How long the user has to configure for black
    while times2 < 41:
        listOfButtons = ev3.buttons.pressed()
        for oneButton in listOfButtons:
            #checks which buton is pressed and what to do
            if oneButton == Button.UP:
                frontColorSensorBlack = p1FSensor.reflection()
                print("Front is " + str(frontColorSensorBlack))


        times2 = times2+0.001
    

    
    print("black has reached")
    #Write values to file
    f = open("ConfiguredColor.txt", "w")
    f.write(str(frontColorSensorWhite)+'\n')
    f.write(str(frontColorSensorBlack)+'\n')
    f.close()