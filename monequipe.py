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

team10=SoccerTeam("osef")
team10.add_player(SoccerPlayer("t10j1",Dat()))
#team10.add_player(SoccerPlayer("t10j2",Wait()))

team20=SoccerTeam("osef")
team20.add_player(SoccerPlayer("t20j1",DefStrat()))
#team20.add_player(SoccerPlayer("t20j2",Test()))
'''



###############################################################################
#1v1
###############################################################################
team1=SoccerTeam("Def")
team1.add_player(SoccerPlayer("t1j1",DefStrat()))

team11=SoccerTeam("Fonceur")
team11.add_player(SoccerPlayer("t11j1",GoAndShoot()))

team111=SoccerTeam("Dat")
team111.add_player(SoccerPlayer("t111j1",Dat()))



###############################################################################
#2v2
###############################################################################

team2=SoccerTeam("Fonceurs")
team2.add_player(SoccerPlayer("t2j1",GoAndShoot()))
team2.add_player(SoccerPlayer("t2j2",GoAndShoot()))


team22=SoccerTeam("Dat Def")
team22.add_player(SoccerPlayer("t22j1",DefStrat()))
team22.add_player(SoccerPlayer("t22j2",Dat()))

###############################################################################
#4v4
###############################################################################

team4=SoccerTeam("Mauro Chupame La Pija 4v4")
team4.add_player(SoccerPlayer("t4j1", DefStrat()))
team4.add_player(SoccerPlayer("t4j2", DefStrat()))
team4.add_player(SoccerPlayer("t4j3", Dat()))
team4.add_player(SoccerPlayer("t4j4", GoAndShoot()))

team5=SoccerTeam("4v4 super attaque maggle")
team5.add_player(SoccerPlayer("t5j1", Dat()))
team5.add_player(SoccerPlayer("t5j2", Dat()))
team5.add_player(SoccerPlayer("t5j3", GoAndShoot()))
team5.add_player(SoccerPlayer("t5j4", GoAndShoot()))
''


teams=[team1, team11, team111, team2, team22, team4, team5]
name="Maccabi"