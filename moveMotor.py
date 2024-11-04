#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Define ports for motors
leftWheel = Motor(Port.A)
rightWheel = Motor(Port.B)

pusherMotor = Motor(Port.C)

# Define drivebase specifications -> Axel track is the distance between the wheels
robot = DriveBase(leftWheel, rightWheel, wheel_diameter = 55.5, axel_track=104)

# Write your program here.

# Drive forward and backwards 200mm
robot.straight(200)
robot.straight(-200)

# Spin around clockwise and then anti-clockwise
robot.turn(360)
robot.turn(-360)

# Run the push motor at 300 deg/s, until it is stopped
pusherMotor.run(300)
time.sleep(1000)
pusherMotor.stop()

# Use a for loop to specify how many times the same code should be run
for counter in range(6):
    pusherMotor.run_time(300,1000)
    time.sleep(1000)