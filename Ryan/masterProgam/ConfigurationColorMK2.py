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
p1FSensor = ColorSensor(Port.S1)
p2BSensor = ColorSensor(Port.S2)
p3SSensor = ColorSensor(Port.S3)
def colorConfigMK2():

    frontWhite = 0
    sideWhite = 0
    backWhite = 0

    while frontWhite == 0 or sideWhite == 0 or backWhite == 0:
        listOfButtons = ev3.buttons.pressed()
        for oneButton in listOfButtons:
            print(oneButton)
            if oneButton == Button.RIGHT:
                sideWhite = p1FSensor.reflection()
                print("Side value is: " + str(sideWhite))
            elif oneButton == Button.UP:
                frontWhite = p2BSensor.reflection()
                print("Front value is: " + str(frontWhite))
            elif oneButton == Button.DOWN:
                backWhite = p3SSensor.reflection()
                print("Back value is: " + str(backWhite))
    print("White sensing is done.")            
    time.sleep(2)

    print("Starting sensing for black.")
    frontBlack = 0
    sideBlack = 0
    backBlack = 0

    while frontBlack == 0 or sideBlack == 0 or backBlack == 0:
        listOfButtons = ev3.buttons.pressed()
        for oneButton in listOfButtons:
            print(oneButton)
            if oneButton == Button.RIGHT:
                sideBlack = p1FSensor.reflection()
                print("Side value is: " + str(sideBlack))
            elif oneButton == Button.UP:
                frontWhite = p2BSensor.reflection()
                print("Front value is: " + str(frontBlack))
            elif oneButton == Button.DOWN:
                backWhite = p3SSensor.reflection()
                print("Back value is: " + str(backBlack))
    print("Black sensing is done.")

    #Write values to file
    f = open("ConfiguredColor.txt", "w")
    f.write(str(frontColorSensorWhite)+'\n')
    f.write(str(backColorSensorWhite)+'\n')
    f.write(str(sideColorSensorWhite)+'\n')
    f.write(str(frontColorSensorBlack)+'\n')
    f.write(str(backColorSensorBlack)+'\n')
    f.write(str(sideColorSensorBlack)+'\n')
    f.close()