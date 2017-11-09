from __future__ import division
import threading
import time
from src.robot import Robot
from src.drawing import Map, Canvas
import brickpi

#Initialize the interface
interface=brickpi.Interface()
interface.initialize()

PARTICLES = None

MAP = [[0,0,"O"],
       [0,168,"A"],
       [84,168,"B"],
       [84,126,"C"],
       [84,210,"D"],
       [168,210,"E"],
       [168,84,"F"],
       [210,84,"G"],
       [210,0,"H"]]

POINTS = [(84,30),
          (180,30),
          (180,53),
          (138,54),
          (138,168),
          (114,168),
          (114,84),
          (84,84),
          (84,30),
          (0,0)]

Robot = Robot(interface,
              pid_config_file="carpet_config.json",
              map=MAP,
              mcl=True,
              x= 20,
              y=20,
              mode="continuous",
              theta=90,
              threading=True
              )

Canvas = Canvas();
Map = Map();
Map.add_wall((0,0,0,168));        # a
Map.add_wall((0,168,84,168));     # b
Map.add_wall((84,126,84,210));    # c
Map.add_wall((84,210,168,210));   # d
Map.add_wall((168,210,168,84));   # e
Map.add_wall((168,84,210,84));    # f
Map.add_wall((210,84,210,0));     # g
Map.add_wall((210,0,0,0));        # h
Map.draw();


for x,y in POINTS:
    Robot.navigate_to_waypoint(x/100,y/100)
    NUMBER_OF_PARTICLES = Robot.get_state()
    canvas.drawParticles(NUMBER_OF_PARTICLES):

interface.terminate()
