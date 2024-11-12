#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()


# Question 1
# I have two wheels in my robot, one on Port A and one on Port B and a pushing motor on Port C
# Can you set up those for me?
leftWheel = Motor(Port.A)
rightWheel = Motor(Port.B)
pusherMotor = Motor(Port.C)

# Can you set up my robot drivebase for me? The wheel diameter is 55.5mm and the distance between the wheels is 104mm.
robot = DriveBase(leftWheel, rightWheel, wheel_diameter = 55.5, axel_track=104)

# I have a touch sensor on Port S1 and an ultrasonic sensor on Port S2. Can you set those up for me?
touchSensor = TouchSensor(Port.S1)
ultrasonicSensor = UltrasonicSensor(Port.S2)

# Question 2
# Can you write an if statement that will make the robot drive forward 100mm if the touch sensor is pressed?
if touchSensor.pressed():
    robot.drive(100)

# Question 3
# Can you write a loop to check if the ultrasonic sensor reads a distance less than 10mm and if it does make the robot spin in a circle?
while ultrasonicSensor.distance() < 10:
    robot.turn(360)

# Question 4
# Can you write a loop that will make the robot drive forward 100mm and then stop for 1 second, and then repeat this 5 times?
for i in range(6):
    robot.straight(100)
    wait(1000)