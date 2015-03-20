# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 11:42:52 2015
"""

from soccersimulator import pyglet
from soccersimulator import PygletObserver
from soccersimulator import SoccerBattle, SoccerTeam, SoccerPlayer
from td1 import *

'''
###############################################################################
#Testing (T1 ROUGE - T2 BLEU)
###############################################################################

team1=SoccerTeam("Messi")
team1.add_player(SoccerPlayer("Goal",Messi()))
#team1.add_player(SoccerPlayer("t1j2",Messi()))
#team1.add_player(SoccerPlayer("t1j3",DefStrat()))
#team1.add_player(SoccerPlayer("t1j4",Messi()))

team2=SoccerTeam("Fonceur")
team2.add_player(SoccerPlayer("Atta",Fonceur()))
#team2.add_player(SoccerPlayer("t2j2",DefStrat()))
#team2.add_player(SoccerPlayer("t2j3",DefStrat()))
#team2.add_player(SoccerPlayer("t2j4",DefStrat()))



teams=[team1, team2]
name="Maccabi"

'''

###############################################################################
#1v1
###############################################################################


team11=SoccerTeam("Fonceur")
team11.add_player(SoccerPlayer("t11j1",Fonceur()))

team111=SoccerTeam("Messi")
team111.add_player(SoccerPlayer("t111j1",Messi()))



###############################################################################
#2v2
###############################################################################

team2=SoccerTeam("Fonceurs")
team2.add_player(SoccerPlayer("t2j1",Fonceur()))
team2.add_player(SoccerPlayer("t2j2",Fonceur()))



team222=SoccerTeam("Def")
team222.add_player(SoccerPlayer("t222j1",Fonceur()))
team222.add_player(SoccerPlayer("t222j2",Messi()))

team2222=SoccerTeam("Double Messi")
team2222.add_player(SoccerPlayer("t2222j1",Messi()))
team2222.add_player(SoccerPlayer("t2222j2",Messi()))

###############################################################################
#4v4
###############################################################################

team4=SoccerTeam("Def de retard")
team4.add_player(SoccerPlayer("t4j1", Fonceur()))
team4.add_player(SoccerPlayer("t4j2", Messi()))
team4.add_player(SoccerPlayer("t4j3", Messi()))
team4.add_player(SoccerPlayer("t4j4", Fonceur()))

team5=SoccerTeam("attaque de retard")
team5.add_player(SoccerPlayer("t5j1", Fonceur()))
team5.add_player(SoccerPlayer("t5j2", Fonceur()))
team5.add_player(SoccerPlayer("t5j3", Fonceur()))
team5.add_player(SoccerPlayer("t5j4", Fonceur()))



teams=[team11, team111, team2, team222, team2222, team4, team5]
name="Maccabi"