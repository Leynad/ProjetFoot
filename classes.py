# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 18:48:14 2015

@author: 3301097
"""

from soccersimulator import Vector2D, SoccerAction, SoccerStrategy, pyglet
from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam 
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS

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
        
class JoueurFonceur(SoccerStrategy):
    def __init__(self):
        self.name="Random"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        position = state.ball.position - player.position
        shoot = Vector2D(0,0)
        if (PLAYER_RADIUS+BALL_RADIUS)>=(state.ball.position.distance(player.position)):
            teamadverse=2
            if teamid==1:
                teamadverse=1
                shoot= (state.get_goal_center(teamadverse)-player.position)
        return SoccerAction(pos,shoot)
    def copy(self):
        return JoueurFonceur()
    def create_strategy(self):
        return JoueurFonceur()
        
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