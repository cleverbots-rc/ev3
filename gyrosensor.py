#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Define ports for motors
leftWheel = Motor(Port.A)
rightWheel = Motor(Port.B)

# Define ports for sensors
gyroSensor = GyroSensor(Port.S4)

# Define drivebase specifications -> Axel track is the distance between the wheels
robot = DriveBase(leftWheel, rightWheel, wheel_diameter = 55.5, axel_track=104)


# Write your program here.

# TO DO: Figure out to make gyro work in a way that is remotely usable
while True:
    robot.turn(600)

    if gyroSensor.angle() == 360:
        robot.stop()
        break