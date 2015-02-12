# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 18:48:14 2015

@author: 3301097
"""

from soccersimulator import Vector2D, SoccerAction, SoccerStrategy, pyglet
from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam 
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS
import need, random, math

#######################################################
#RANDOM
######################################################

class Random(SoccerStrategy):
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
        return Random()
    def create_strategy(self):
        return Random()
        
########################################################
#joueurFonceur
########################################################  
      
class JoueurFonceur(SoccerStrategy):
    def __init__(self):
        self.name="Fonceur"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        acceleration = state.ball.position - player.position
        shoot = Vector2D(0,0)
        if (PLAYER_RADIUS+BALL_RADIUS)>=(state.ball.position.distance(player.position)):
            shoot= (state.get_goal_center(need.teamAdverse(teamid))-player.position)
        return SoccerAction(acceleration,shoot)
    def copy(self):
        return JoueurFonceur()
    def create_strategy(self):
        return JoueurFonceur()

      
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
            
            shoot = (state.get_goal_center(need.teamAdverse(teamid)) - posBall).product(100000)
                
        return SoccerAction(acceleration, shoot)
    def copy(self):
        return JoueurFonceur()
    def create_strategy(self):
        return JoueurFonceur()    

#################################################
#Class de stratégie de base : Se déplace vers un point
################################################

class AllerVersPoint(SoccerStrategy):
    def __init__(self, zone):
        self.name="Random"
        self.zone = zone
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        self.zone #Créer Vector2D au bon endroit strat = AllerVersPoint(Vector2D(**,**))
        acceleration = self.zone - player.position
        shoot = Vector2D(0,0)
        return SoccerAction(acceleration, shoot)
    def copy(self):
        return AllerVersPoint(self.zone)
    def create_strategy(self):
        return AllerVersPoint(self.zone)
        
################################        
#Anda a la PELOTA carajo !
###############################

class AllerVersPelota(SoccerStrategy):
    def __init__(self):
        self.name="AllerVersPelota"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        shoot = Vector2D()
        pos = state.ball.position-player.position
        return SoccerAction(pos,shoot)
    def copy(self):
        return AllerVersPelota()
    def create_strategy(self):
        return AllerVersPelota()
        

        
######################################
#Pour tir
######################################

class Shoot(SoccerStrategy):
    def __init__(self):
        self.name="shoot"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        shoot = state.get_goal_center(need.teamAdverse(teamid))
        return SoccerAction(Vector2D(0,0), shoot)
    def copy(self):
        return Shoot()
    def create_strategy(self):
        return Shoot()
        

################################################
#Stratégie defensive
##############################################

class DefStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Def"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        d = state.ball.position - player.position
        if d.norm > 10:
            acceleration = state.ball.position + state.get_goal_center(teamid) - player.position - player.position
            
        else:
            acceleration = state.ball.position - player.position

        shoot = Vector2D(0,0)
        if (PLAYER_RADIUS+BALL_RADIUS)>=(state.ball.position.distance(player.position)):
            shoot= (state.get_goal_center(need.teamAdverse(teamid))-player.position)
        return SoccerAction(acceleration, shoot)
    def copy(self):
        return DefStrategy()
    def create_strategy(self):
        return DefStrategy()    
        
########################################
#Compose strat
###################################

class ComposeStrategy(SoccerStrategy):
    def __init__(self, strategy1, strategy2):
        self.strategy1 = strategy1
        self.strategy2 = strategy2
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        strategy1 = self.strategy1.compute_strategy(state,player,teamid)
        strategy2 = self.strategy2.compute_strategy(state,player,teamid)
        return SoccerAction(strategy1,strategy2)
    def create_strategy(self):
        return ComposeStrategy()
          
#############################
#Test
########################

class TestStrat(SoccerStrategy):
    def __init__(self):
        self.name="Testeur"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        d = state.ball.position - player.position
        if d.norm > 15:
            acceleration = Vector2D((1.2/5)*GAME_WIDTH,state.ball.position.y)-player.position
            
        else:
            acceleration = state.ball.position - player.position

        shoot = Vector2D(0,0)
        if (PLAYER_RADIUS+BALL_RADIUS)>=(state.ball.position.distance(player.position)):
            shoot= (state.get_goal_center(need.teamAdverse(teamid))-player.position)
        return SoccerAction(acceleration, shoot)
            
    def copy(self):
        return TestStrat()
    def create_strategy(self):
        return TestStrat()
        
#######################
# Defenseur qui tir la balle sur un coté
#######################        
        
class TirAngle(SoccerStrategy):
    def __init__(self):
        self.name="Goal"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        shoot = Vector2D.create_polar(player.angle + 2.5, 100)
        return SoccerAction(Vector2D(5,15), shoot)
    def copy(self):
        return TirAngle()
    def create_strategy(self):
        return TirAngle()
        
###
#Goal
###

class Goal(SoccerStrategy):
    def __init__(self):
        self.name="Goal"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
            a=(state.ball.position+state.get_goal_center((teamid)))
            a.x=a.x/2
            a.y=a.y/2
            a=a-player.position
            shoot = Vector2D.create_polar(6,(teamid-1.5)*20)
            return SoccerAction(a,shoot) #Soit il tir a 10 soit a -10 en fonction de son équipe
    def copy(self):
        return Goal()
    def create_strategy(self):
        return Goal()   
        
#########
#Wait
########

class Wait(SoccerStrategy):
    def __init__(self):
        self.name="Wait"      
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return SoccerAction(Vector2D(0,0),Vector2D(0,0))
    def copy(self):
        return Wait()