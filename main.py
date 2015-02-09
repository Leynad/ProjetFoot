# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 19:12:49 2015

@author: 3301097
"""
from soccersimulator import pyglet
from soccersimulator import PygletObserver
from soccersimulator import SoccerBattle
from td1 import *

from monequipe import teams
team1=teams[0]
team2=teams[1]
battle=SoccerBattle(team1,team2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()