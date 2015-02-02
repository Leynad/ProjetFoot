# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 18:48:14 2015

@author: 3301097
"""

from soccersimulator import Vector2D, SoccerAction, SoccerStrategy, pyglet
from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam 
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS

#######################################################
#RANDOM
######################################################

class RandomStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Random"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        acceleration=Vector2D.create_random(-1, 1)
        shoot=Vector2D.create_random(-1, 1)
        action=SoccerAction(acceleration, shoot)
        return action
    def copy(self):
        return RandomStrategy()
    def create_strategy(self):
        return RandomStrategy()
        
########################################################
#joueurFonceur
########################################################  
      
class JoueurFonceur(SoccerStrategy):
    def __init__(self):
        self.name="Random"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        acceleration = state.ball.position - player.position
        shoot = Vector2D(0,0)
        if (PLAYER_RADIUS+BALL_RADIUS)>=(state.ball.position.distance(player.position)):
            shoot= (state.get_goal_center(self.goal_adverse(teamid))-player.position)
        return SoccerAction(acceleration,shoot)
    def copy(self):
        return JoueurFonceur()
    def create_strategy(self):
        return JoueurFonceur()
    def goal_adverse(self, teamid):
        if teamid == 1:
            return 2
        else:
            return 1
      
##################################################
#JoueurFonceur qui tir (aucune utilité pour le moment)
#################################################
        
class JoueurFonceurTir(SoccerStrategy):
    def __init__(self):
        self.name="Random"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        posPlayer = player.position
        posBall = state.ball.position
        acceleration = (posBall - posPlayer)
        shoot = Vector2D(0,0)
        if((posBall - posPlayer).norm <= PLAYER_RADIUS + BALL_RADIUS):
            teamAdverse = 2
            if teamid == 2:
                teamAdverse = 1
            shoot = (state.get_goal_center(teamAdverse) - posBall).product(100000)
                
        return SoccerAction(acceleration, shoot)
    def copy(self):
        return JoueurFonceur()
    def create_strategy(self):
        return JoueurFonceur()    

#################################################
#Class de stratégie de base : Aller vers un point
################################################

class AllerVersPoint(SoccerStrategy):
    def __init__(self, destination):
        self.name="Random"
        self.destination = destination
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        self.destination #Créer Vector2D au bon endroit strat = AllerVersPoint(Cevtor2D(**,**))
        acceleration = self.destination - player.position
        shoot = Vector2D(0,0)
        return SoccerAction(acceleration, shoot)
    def copy(self):
        return AllerVersPoint(self.destination)
    def create_strategy(self):
        return AllerVersPoint(self.destination)
        
######################################
#Tir
######################################

"""class Tir(SoccerStrategy):
    def __init__(self, destination):
"""

################################################
#Stratégie defensive
##############################################

class DefStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Random"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        d = state.ball.position - player.position
        if d.norm > 25:
            acceleration = state.ball.position + state.get_goal_center(teamid) - player.position - player.position
        else:
            acceleration = state.ball.position - player.position

        shoot = Vector2D(0,0)
        if (PLAYER_RADIUS+BALL_RADIUS)>=(state.ball.position.distance(player.position)):
            shoot= (state.get_goal_center(self.goal_adverse(teamid))-player.position)
        return SoccerAction(acceleration, shoot)
    def copy(self):
        return DefStrategy()
    def create_strategy(self):
        return DefStrategy()
    def goal_adverse(self, teamid):
        if teamid == 1:
            return 2
        else:
            return 1
        
########################################
#compose strat
###################################

class ComposeStrategy(soccerStrategy):
    def __init__(self, strategy1, strategy2):
        self.name="Random"
        self.strategy1 = strategy1
        self.strategy2 = strategy2
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return (state.strategy1, state.strategy2.compute)
    def copy(self):
        return ComposeStrategy(self.strategy1, slef.strategy2)
    def create_strategy(self):
        return ComposeStrategy()
    def goal_adverse(self, teamid):
        if teamid == 1:
            return 2
        else:
            return 1