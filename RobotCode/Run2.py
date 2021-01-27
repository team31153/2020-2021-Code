#!/usr/bin/env pybricks-micropython
# Aaryan and Felix code here.
from TurnGradualGyro import *
from GradualGyroF import *
from GradualGyroB import *
from ColorSensorFunctions import *
from GyroB import *
from GyroF import *

readAllValues()

# Code Here.
def Run2():
    gradualGyroForward(570, 300)
    sideLineFollowerRun1(90) # Line following to just before step counter (line follow for accuracy)
    gyroForward(62, 120)
    gyroForward(35, 20)
    gradualGyroForward(170, 93) # Step counter
    gradualGyroBackward(125, 150) # Back away from step counter
    robot.turn(110)
    gradualGyroForward(140, 160)
    robot.turn(-80)
    frontLineFollowerStopWithSide(60) # line following to align
    robot.turn(103)
    gradualGyroForward(115, 140)
    robot.turn(-101)
    stopOnWhiteBForward()
    stopOnBlackBForward() #align with tire flip
    aMotor.run_angle(7000, 2800)
    gradualGyroForward(260, 100)
    gradualGyroBackward(100, 220)
    aMotor.run_angle(7000, -1300) #Finished tire flip
    # begin align for mission three and four, treadmill and rowing machine
    gradualGyroBackward(140, 200) 
    robot.turn(-90)
    gradualGyroForward(60, 100)
    frontLineFollowerStopWithSide(53) #aligning with end of line closest to treadmill
    gradualGyroBackward(60, 240)
    turnGradualGyro(-40)
    gradualGyroForward(121, 200)
    turnGradualGyro(38)
    robot.straight(210) # Finished alignment
    t1 = Thread(target=aMotor.run_angle, args=([8000, 1300])) # Running both medium motors in parallel to save time
    t1.start()
    bMotor.run_angle(1050, -6600) #Finished Treadmill
    robot.straight(-70)
    turnGradualGyro(13)
    robot.straight(-110) #Pulled rowing machine's tire into small circle
    wait(30)
    aMotor.run_angle(8000, -2200)
    robot.turn(45)
    t2 = Thread(target=aMotor.run_angle, args=([8000, -600])) # Lifting up medium motor while heading back to base
    t2.start()
    gradualGyroBackward(1600, 900)

#Run2()