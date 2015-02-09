# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 11:42:52 2015

@author: 3301097
"""

from soccersimulator import pyglet
from soccersimulator import PygletObserver
from soccersimulator import SoccerBattle, SoccerTeam, SoccerPlayer
from td1 import *

team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
team1.add_player(SoccerPlayer("t1j1",AllerVersPoint(Vector2D(10,10))))
team2.add_player(SoccerPlayer("t2j1",RandomStrategy()))
team1.add_player(SoccerPlayer("t1j2",DefStrategy()))
team2.add_player(SoccerPlayer("t2j2",JoueurFonceur()))


teams=[team1,team2]
name="Mon Club"