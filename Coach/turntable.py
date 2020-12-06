#!/usr/bin/env pybricks-micropython

from robot import *

def rotateTurnTableAntiClock(degrees):
    #aMotor.run_angle(50, degrees, Stop.BRAKE, False)
    aMotor.reset_angle(0)
    while aMotor.angle() < degrees:
        aMotor.run(720)
    aMotor.stop()

def rotateTurnTableClock(degrees):
    #aMotor.run_angle(50, degrees, Stop.BRAKE, False)
    aMotor.reset_angle(0)
    degrees = degrees * -1
    while aMotor.angle() > degrees:
        aMotor.run(-720)
    aMotor.stop()
