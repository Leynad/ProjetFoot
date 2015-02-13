# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 11:42:52 2015

@author: 3301097
"""

from soccersimulator import pyglet
from soccersimulator import PygletObserver
from soccersimulator import SoccerBattle, SoccerTeam, SoccerPlayer
from td1 import *

team1=SoccerTeam("Goooo 1v1")
team1.add_player(SoccerPlayer("t1j1",GoAndShoot()))

team2=SoccerTeam("Dat Fonceur 2v2")
team2.add_player(SoccerPlayer("t2j1",GoAndShoot()))
team2.add_player(SoccerPlayer("t2j2",DefStrat()))


team4=SoccerTeam("Mauro Chupame La Pija 4v4")
team4.add_player(SoccerPlayer("t4j1", DefStrat()))
team4.add_player(SoccerPlayer("t4j2", GoAndShoot()))
team4.add_player(SoccerPlayer("t4j3", GoAndShoot()))
team4.add_player(SoccerPlayer("t4j4", GoAndShoot()))

teams=[team1,team2, team4]
name="Maccabi"