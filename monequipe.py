# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 11:42:52 2015
"""

from soccersimulator import *
from td1 import *
from apprentissage import *

'''
###############################################################################
#Testing (T1 ROUGE - T2 BLEU)
###############################################################################

team1=SoccerTeam("Messi")
#team1.add_player(SoccerPlayer("Goal",Fonceur()))
#team1.add_player(SoccerPlayer("t1j2",Wait()))
#team1.add_player(SoccerPlayer("t1j3",DefStrat()))
#team1.add_player(SoccerPlayer("t1j4",Messi()))

#team2=SoccerTeam("Fonceur")
#team2.add_player(SoccerPlayer("Atta",Wait()))
#team2.add_player(SoccerPlayer("t2j2",DefStrat()))
#team2.add_player(SoccerPlayer("t2j3",DefStrat()))
#team2.add_player(SoccerPlayer("t2j4",DefStrat()))

team_tree = SoccerTeam("Team Tree")

treeia=TreeIA(gen_feature_simple,dict({"Fonceur":Fonceur(),"DefStratBis":DefStratBis()}))
### Apprentissage
fn=os.path.join(os.path.dirname(os.path.realpath(__file__)),"best_goal.pkl")
treeia.load(fn)
TreeST=TreeStrategy("tree1",treeia)

team_tree.add_player(SoccerPlayer("Tree 1",TreeST))
team_tree.add_player(SoccerPlayer("Tree 2",TreeST))


teams=[team1, team_tree]
name="Maccabi"
'''




###############################################################################
#Equipe IA
###############################################################################

team_tree = SoccerTeam("Team Tree")

treeia=TreeIA(gen_feature_simple,dict({"Fonceur":Fonceur(),"DefStratBis":DefStratBis()}))
### Apprentissage
fn=os.path.join(os.path.dirname(os.path.realpath(__file__)),"best_goal.pkl")
treeia.load(fn)
TreeST=TreeStrategy("tree1",treeia)

team_tree.add_player(SoccerPlayer("Tree 1",TreeST))
team_tree.add_player(SoccerPlayer("Tree 2",TreeST))

###############################################################################
#1v1
###############################################################################

team2=SoccerTeam("FonceurPoto")
team2.add_player(SoccerPlayer("Poteau",FonceurPoto()))

team3=SoccerTeam("GoalPower")
team3.add_player(SoccerPlayer("GoalPower",GoalPower()))

team4=SoccerTeam("DefPower")
team4.add_player(SoccerPlayer("DefPower",DefPower()))




###############################################################################
#2v2
###############################################################################

team5=SoccerTeam("Defensive")
team5.add_player(SoccerPlayer("GoalPower",GoalPower()))
team5.add_player(SoccerPlayer("DefPower",DefPower()))

team6=SoccerTeam("One")
team6.add_player(SoccerPlayer("poto",FonceurPoto()))
team6.add_player(SoccerPlayer("Goal",GoalPower()))

team7=SoccerTeam("Two")
team7.add_player(SoccerPlayer("poto",FonceurPoto()))
team7.add_player(SoccerPlayer("Goal",DefPower()))

team11=SoccerTeam("Reeetard")
team11.add_player(SoccerPlayer("poto",FonceurPoto()))
team11.add_player(SoccerPlayer("Goal",FonceurPoto()))




###############################################################################
#4v4
###############################################################################

team8=SoccerTeam("Atta")
team8.add_player(SoccerPlayer("t4j1", FonceurPoto()))
team8.add_player(SoccerPlayer("t4j2", FonceurPoto()))
team8.add_player(SoccerPlayer("t4j3", DefPower()))
team8.add_player(SoccerPlayer("t4j4", GoalPower()))

team9=SoccerTeam("Defensive")
team9.add_player(SoccerPlayer("t5j1", DefStratBis()))
team9.add_player(SoccerPlayer("t5j2", DefPower()))
team9.add_player(SoccerPlayer("t5j3", Defenseur()))
team9.add_player(SoccerPlayer("t5j4", GoalPower()))

team10=SoccerTeam("MegaDefensive")
team10.add_player(SoccerPlayer("t5j1", GoalPower()))
team10.add_player(SoccerPlayer("t5j2", DefStratBis()))
team10.add_player(SoccerPlayer("t5j3", Defenseur()))
team10.add_player(SoccerPlayer("t5j4", FonceurPoto()))

team12=SoccerTeam("Retard")
team12.add_player(SoccerPlayer("Atta",FonceurPoto()))
team12.add_player(SoccerPlayer("Defenseur",FonceurPoto()))
team12.add_player(SoccerPlayer("t2j3",FonceurPoto()))
team12.add_player(SoccerPlayer("t2j4",FonceurPoto()))



teams=[team2, team3, team4, team5, team6, team7, team8, team9, team10, team11, team12,team_tree]
name="Maccabi"
