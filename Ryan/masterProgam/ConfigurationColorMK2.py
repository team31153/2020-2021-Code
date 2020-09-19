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

    frontWhite = -1000
    sideWhite = -1000
    backWhite = -1000

    while frontWhite == -1000 or sideWhite == -1000 or backWhite == -1000:
        listOfButtons = ev3.buttons.pressed()
        for oneButton in listOfButtons:
            print(oneButton)
            if oneButton == Button.RIGHT:
                sideWhite = p3SSensor.reflection()
                print("Side value is: " + str(sideWhite))
            elif oneButton == Button.UP:
                frontWhite = p1FSensor.reflection()
                print("Front value is: " + str(frontWhite))
            elif oneButton == Button.DOWN:
                backWhite = p2BSensor.reflection()
                print("Back value is: " + str(backWhite))
    print("White sensing is done.")            
    time.sleep(2)

    print("Starting sensing for black.")
    frontBlack = 1000
    sideBlack = 1000
    backBlack = 1000

    while frontBlack == 1000 or sideBlack == 1000 or backBlack == 1000:
        listOfButtons = ev3.buttons.pressed()
        for oneButton in listOfButtons:
            print(oneButton)
            if oneButton == Button.RIGHT:
                sideBlack = p3SSensor.reflection()
                print("Side value is: " + str(sideBlack))
            elif oneButton == Button.UP:
                frontBlack = p1FSensor.reflection()
                print("Front value is: " + str(frontBlack))
            elif oneButton == Button.DOWN:
                backBlack = p2BSensor.reflection()
                print("Back value is: " + str(backBlack))
    print("Black sensing is done.")
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