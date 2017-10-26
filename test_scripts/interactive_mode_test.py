import threading
import time
import sys
from src.robot import Robot
import brickpi

#Initialize the interface
interface=brickpi.Interface()
interface.initialize()
interface.startLogging("motor_position_1.log")

Robot = Robot(interface,'carpet_config.json')


Robot.interactive_mode()

interface.stopLogging()
interface.terminate()
