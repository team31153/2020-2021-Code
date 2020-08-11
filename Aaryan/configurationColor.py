#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

ev3 = EV3Brick()
cMotor = Motor(Port.C)
dMotor = Motor(Port.D)
aMotor = Motor(Port.A)
bMotor = Motor(Port.B)
gyro = GyroSensor(Port.S4)
frontColorSensor = ColorSensor(Port.S3)
backColorSensor = ColorSensor(Port.S2)
robot = DriveBase(cMotor, dMotor, 56, 60)

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
config()
        
                
        
    
        
    