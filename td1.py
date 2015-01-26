# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ce script temporaire est sauvegardé ici :
/users/Etu7/3301097/.spyder2/.temp.py
"""
from soccersimulator import Vector2D, SoccerAction, SoccerStrategy, pyglet
from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam 
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS
v=Vector2D(10, 5)
u=Vector2D(6, 3)

v.norm

acceleration=Vector2D(10, 7)
shoot=Vector2D(15, 8)

action=SoccerAction(acceleration, shoot)

pos=Vector2D.create_random()
shoot=Vector2D.create_random()
action=SoccerAction(pos, shoot)

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
        pass1
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
            shoot = (state.get_goal_center(teamAdverse) - posBall)
        return SoccerAction(acceleration, shoot)
    def copy(self):
        return JoueurFonceur()
    def create_strategy(self):
        return JoueurFonceur()
        

        

team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
team1.add_player(SoccerPlayer("t1j1",JoueurFonceur()))
team2.add_player(SoccerPlayer("t2j1",RandomStrategy()))
team1.add_player(SoccerPlayer("t1j2",RandomStrategy()))
team2.add_player(SoccerPlayer("t2j2",RandomStrategy()))
battle=SoccerBattle(team1,team2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()

