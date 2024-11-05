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
pusherMotor = Motor(Port.C)

# Write your program here.

# Run the push motor at 300 deg/s, until it is stopped
pusherMotor.run(300)
wait(1000)
pusherMotor.stop()

# Use a for loop to specify how many times the same code should be run
for counter in range(6):
    pusherMotor.run_time(300,1000)
    wait(1000)