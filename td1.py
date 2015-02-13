# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 18:48:14 2015

@author: 3301097
"""

from soccersimulator import Vector2D, SoccerAction, SoccerStrategy, pyglet
from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam 
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS, GAME_HEIGHT, GAME_WIDTH
import need, random, math


##########
#Si besoin (en fonction de certaines vieilles classes)
###########

def teamAdverse(teamid):
    adv=2
    if (teamid==2):
        adv=1
    return adv

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
#joueurFonceur but GoalAndShoot plus fort
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

#################################################
#Se déplace vers un point
################################################

class AllerVersPoint(SoccerStrategy):
    def __init__(self, zone):
        self.name="Random"
        self.point = point
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        self.point 
        #Créer Vector2D au bon endroit strat = AllerVersPoint(Vector2D(**,**))
        acceleration = self.point - player.position
        shoot = Vector2D(0,0)
        return SoccerAction(acceleration, shoot)
    def copy(self):
        return AllerVersPoint(self.point)
    def create_strategy(self):
        return AllerVersPoint(self.point)
        
################################        
#Anda a la PELOTA carajo !
###############################

class GoToBall(SoccerStrategy):
    def __init__(self):
        self.name="pelota"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        shoot = Vector2D()
        pos = state.ball.position-player.position
        return SoccerAction(pos,shoot)
    def copy(self):
        return GoToBall()
    def create_strategy(self):
        return GoToBall()
        

        
######################################
#Pour tirer vers le but adverse
######################################

class Shoot(SoccerStrategy):
    def __init__(self):
        self.name="shoot"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        shoot = state.get_goal_center(need.teamAdverse(teamid)) - player.position
        return SoccerAction(Vector2D(0,0), shoot)
    def copy(self):
        return Shoot()
    def create_strategy(self):
        return Shoot()
        
########################################
#Compose strat : go & shooter
###################################

class ComposeStrategy(SoccerStrategy):
    def __init__(self, move, tir):
        self.move = move
        self.tir = tir
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        move = self.move.compute_strategy(state,player,teamid)
        tir = self.tir.compute_strategy(state,player,teamid)
        return SoccerAction(move.acceleration, tir.shoot)
    def copy(self):
        return PelotaShoot()
    def create_strategy(self):
        return ComposeStrategy()

        
############################################
#Compo 2 strats : GoToBall and Shoot 
############################################

class GoAndShoot(SoccerStrategy):
    def __init__(self):
        self.goball = ComposeStrategy(GoToBall(), Shoot())
        #self.tirball = ComposeStrategy(GoToBall(), Shoot())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        #pos_goal = state.get_goal_center(need.teamAdverse(teamid))
        #pos_ball = state.ball.position
        #pg_pb = pos_goal - pos_ball
        #if ()
        return self.goball.compute_strategy(state, player, teamid)
    def copy(self):
        return GoAndShoot()
    def create_strategy(self):
        return GoAndShoot()

###########################
#Defstrat en cas de besoin
##########################
'''
class DefIntell(SoccerStrategy):
    def __init__(self):
        self.goball = ComposeStrategy(GoToBall(), Shoot())
        self.godef=DefStrat()
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        #pos_goal = state.get_goal_center(need.teamAdverse(teamid))
        pos_ball = state.ball.position
        #pg_pb = pos_goal - pos_ball
        if(pos_ball.x > (GAME_WIDTH/3.O):
            return self.godef.compute_strategy(state, player, teamid)
        return self.goball.compute_strategy(state, player, teamid)
    def copy(self):
        return DefIntell()
    def create_strategy(self):
        return DefIntell()
'''
################################################
#Stratégie defensive
##############################################

class DefStrat(SoccerStrategy):
    def __init__(self):
        self.name="Def"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        shoot = Vector2D(0,0)
        d = state.ball.position - player.position # diff entre ball et joueur
        if d.norm > 25 :
            if (teamAdverse(teamid)==2):
                pos = Vector2D((1.2/5)*GAME_WIDTH,state.ball.position.y)-player.position
            else:
                pos = Vector2D((3.8/5)*GAME_WIDTH,state.ball.position.y)-player.position
        else:
            pos= state.ball.position-player.position
            shoot= (state.get_goal_center(teamAdverse(teamid))-player.position)
        if (PLAYER_RADIUS+BALL_RADIUS)>=(state.ball.position.distance(player.position)):
            shoot= (state.get_goal_center(teamAdverse(teamid))-player.position)
        return SoccerAction(pos,shoot)
    def copy(self):
        return DefStrat()
    def create_strategy(self):
        return DefStrat()

#######################
# Tir la balle sur un coté (aléatoir)
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
    def create_strategy(self):
        return Wait()      