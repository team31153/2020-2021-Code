#!/usr/bin/env pybricks-micropython

from robot import *
from stopOnBlack import *
from signal import *
from turntable import *

from multiprocessing import Process
from threading import Thread

# Go forward and stop on the front color sensor hitting black
#stopOnBlackFront()

# Signal completion - 3 red blinks
#blinkLights(Color.RED, 3)

# Rotate the turntable
#rotateTurnTableAntiClock(3600)
#rotateTurnTableClock(3600)

# Signal completion - 3 orange blinks
#blinkLights(Color.ORANGE, 3)

# p1 = Process(target=stopOnBlackFront, args=())
# p1.start()

# p2 = Process(target=rotateTurnTableClock, args=(3600))
# p2.start()

# p1.join()
# p2.join()

t1 = Thread(target=stopOnBlackFront, args=())
t1.start()

#t2 = Thread(target=rotateTurnTableClock, args=(3600))
#t2.start()
rotateTurnTableAntiClock(3600)
#rotateTurnTableClock(3600)

#t1.join()
#t2.join()

# Signal completion - 3 yello blinks
blinkLights(Color.YELLOW, 3)
