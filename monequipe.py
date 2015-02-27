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
team10.add_player(SoccerPlayer("t10j1",DefStrat()))
#team10.add_player(SoccerPlayer("t10j2",Wait()))

team20=SoccerTeam("osef")
team20.add_player(SoccerPlayer("t20j1",Dat()))
#team20.add_player(SoccerPlayer("t20j2",Test()))


'''


###############################################################################
#1v1
###############################################################################

team1=SoccerTeam("Fonceur")
team1.add_player(SoccerPlayer("t1j1",GoAndShoot()))

team11=SoccerTeam("Dat")
team11.add_player(SoccerPlayer("t11j1",Dat()))

team111=SoccerTeam("Def")
team111.add_player(SoccerPlayer("t111j1",DefStrat()))
'''
###############################################################################
#2v2
###############################################################################

team1=SoccerTeam("Fonceurs")
team1.add_player(SoccerPlayer("t1j1",GoAndShoot()))
team1.add_player(SoccerPlayer("t1j2",GoAndShoot()))

team3=SoccerTeam("Messi")
team3.add_player(SoccerPlayer("t3j1",Messi()))
team3.add_player(SoccerPlayer("t3j2",Messi()))

team6=SoccerTeam("Mixt off")
team6.add_player(SoccerPlayer("t6j1",Messi()))
team6.add_player(SoccerPlayer("t6j2",GoAndShoot()))

team2=SoccerTeam("Defensive")
team2.add_player(SoccerPlayer("t2j1",DefStrat()))
team2.add_player(SoccerPlayer("t2j2",DefStratV2()))

###############################################################################
#4v4
###############################################################################

team4=SoccerTeam("Mauro Chupame La Pija 4v4")
team4.add_player(SoccerPlayer("t4j1", DefStrat()))
team4.add_player(SoccerPlayer("t4j2", DefStratV2()))
team4.add_player(SoccerPlayer("t4j3", GoAndShoot()))
team4.add_player(SoccerPlayer("t4j4", GoAndShoot()))

team5=SoccerTeam("4v4 super attaque maggle")
team5.add_player(SoccerPlayer("t5j1", Messi()))
team5.add_player(SoccerPlayer("t5j2", Messi()))
team5.add_player(SoccerPlayer("t5j3", GoAndShoot()))
team5.add_player(SoccerPlayer("t5j4", GoAndShoot()))
'''


teams=[team1, team11, team111]
name="Maccabi"