"""
Created on Mon Jan 26 19:12:49 2015
"""
from soccersimulator import pyglet
from soccersimulator import PygletObserver
from soccersimulator import SoccerBattle
from soccersimulator import SoccerPlayer, SoccerTeam, InteractStrategy, TreeStrategy
from td1 import *

from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pickle
import os

from soccersimulator import SoccerStrategy


from monequipe import teams

list_key_player1=['a','e']
list_strat_player1=[Fonceur(),DefStratBis()]
inter_strat_player1=InteractStrategy(list_key_player1,list_strat_player1,"best_goal")

team1=SoccerTeam("AI")
team1.add_player(SoccerPlayer("AI",inter_strat_player1))

team2=SoccerTeam("Normal")
team2.add_player(SoccerPlayer("Def", Fonceur()))


teams=[team1, team2]
name="AI Test"

team1=teams[0]
team2=teams[1]
battle=SoccerBattle(team1,team2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()