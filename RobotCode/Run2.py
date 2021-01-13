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
    gradualGyroForward(300, 300)
    sideLineFollowerRun1(90) # Line following to just before step counter (line follow for accuracy)
    wait(10)
    gyroForward(60, 100)
    gradualGyroForward(200, 26) # Step counter
    robot.straight(-90) # Back away from step counter
    robot.turn(110)
    robot.straight(100)
    robot.turn(-80)
    frontLineFollowerStopWithSide(60) # line following to align
    robot.turn(103)
    robot.straight(115)
    robot.turn(-101)
    stopOnWhiteBForward()
    stopOnBlackBForward() #align with tire flip
    aMotor.run_angle(7000, 2800)
    gradualGyroForward(260, 100)
    gradualGyroBackward(80, 200) #180 to 140
    aMotor.run_angle(7000, -1300) #Finished tire flip
    # begin align for mission three and four, treadmill and rowing machine
    robot.straight(-130) #120 to 100
    robot.turn(-90)
    robot.straight(75)
    robot.turn(85)
    frontLineFollowerStopWithSide(60) #aligning with end of line closest to treadmill
    gradualGyroBackward(60, 200)
    turnGradualGyro(-40)
    gradualGyroForward(121, 200)
    turnGradualGyro(37)
    robot.straight(210) # Finished alignment
    t1 = Thread(target=aMotor.run_angle, args=([8000, 1300])) # Running both medium motors in parallel to save time
    t1.start()
    bMotor.run_angle(1050, -6200) #Finished Treadmill
    robot.straight(-70)
    turnGradualGyro(13)
    robot.straight(-110) #Pulled rowing machine's tire into small circle
    wait(30)
    aMotor.run_angle(8000, -2200)
    robot.turn(60)
    t2 = Thread(target=aMotor.run_angle, args=([8000, -600])) # Lifting up medium motor while heading back to base
    t2.start()
    gradualGyroBackward(1600, 700)

#Run2()