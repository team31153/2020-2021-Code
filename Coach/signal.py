#!/usr/bin/env pybricks-micropython
import time

from robot import *

def blinkLights(color, count):
    while count > 0:
        ev3brick.light(color)
        time.sleep(0.5)
        ev3brick.light(None)
        time.sleep(0.5)
        count = count - 1
