#!/usr/bin/env pybricks-micropython
# Aaryan and Felix code here.
from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *
from GyroB import *
from GyroF import *

# ORIGINALLY Run1reset
# RYAN CHANGED IT TO Run2reset ON 1/3/20

readAllValues()
aMotor.run_angle(8000, -2700)
#2400 - 2800