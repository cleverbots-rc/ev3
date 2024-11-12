#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This file is a basic set of code that can be used in the tournament. 
# You should change it to fit your robot's configuration, and what you want it to do. 
# What works for me might not work for you!

# Create your objects here.
ev3 = EV3Brick()

# Define ports for motors
leftWheel = Motor(Port.A)
rightWheel = Motor(Port.B)
pusherMotor = Motor(Port.C)

robot = driveTrain(leftWheel, rightWheel, 55.5, 104)

# Define ports for sensors
ultrasonicSensor = UltrasonicSensor(Port.S1)

# Run the code inside the code block forever

# This function will make the robot turn until it finds an opponent or until 10 loops have passed
def locateOpponent():
    loopsElapsed = 0
    while ultrasonicSensor.distance() > 100 OR loopsElapsed <= 10:
        robot.turn(36)
    if ultrasonicSensor.distance() <= 100:
        return (True, ultrasonicSensor.distance()) # This is called a tuple, it as variable that contains many variables
    else:
        return (False, 0)

# This function will push the opponent using the pusher motor
def pushOpponent():
    pusherMotor.run_target(100, 90)
    robot.straight(300)
    wait(1000)
    pusherMotor.run_target(-100, 0)

# This is the main loop of the program, it uses the two functions above to locate and push the opponent
while True:
    opponentFound, distance = locateOpponent() # This is called tuple unpacking, I need to use two variables to store the results of the function
    # If the opponent is found, push it. If not, drive forward 100mm and stop
    if opponentFound:
        robot.straight(distance)
        pushOpponent()
    else:
        robot.drive(100, 0)
        wait(1000)
        robot.stop()
        robot.turn(360)
    