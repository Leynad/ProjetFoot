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
team3=SoccerTeam("team3")
team4=SoccerTeam("team4")
team1.add_player(SoccerPlayer("t1j1",JoueurFonceur()))
team2.add_player(SoccerPlayer("t2j1",JoueurFonceur()))
team1.add_player(SoccerPlayer("t1j2",JoueurFonceur()))
team2.add_player(SccerPlayer("t2j2",JoueurFonceur()))
team3.add_player(SocerPlayer("t3j1",JoueurFonceur()))
team3.add_player(SoccerPlayer("t3j2",JoueurFonceur()))
team4.add_player(SocerPlayer("t4j1",JoueurFonceur()))
team4.add_player(SoccerPlayer("t4j2",JoueurFonceur()))



teams=[team1,team2, team3, team4]
name="MaccabiTLV"