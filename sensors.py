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

# Define ports for sensors
touchSensor = TouchSensor(Port.S1)
colorSensor = ColorSensor(Port.S2)
ultrasonicSensor = UltrasonicSensor(Port.S3)

# Write your program here.

# Run the code inside the code block forever
while True:
    # Use an if statement to detect if the touch sensor is pressed down
    if touchSensor.pressed():
        ev3.speaker.say("Stop Touching Me")

    # Use an if statement to check if the colour seen by a colour sensor is white
    if colorSensor.color() == Color.WHITE:
        ev3.speaker.say("Looks like there is something white near me")

    # Use an if statement to check if the reflected light is below 25%
    if colorSensor.reflection() <= 25:
        ev3.speaker.say("I can see something pretty dark")

    # Use an if statement to check if there is something within 10mm of the sensor.
    if ultrasonicSensor.distance() > 10:
        ev3.speaker.say("You're really close to me!")