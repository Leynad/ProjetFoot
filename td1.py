# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 18:48:14 2015


"""

from soccersimulator import Vector2D, SoccerAction, SoccerStrategy, pyglet
from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam,GAME_GOAL_HEIGHT 
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS, GAME_HEIGHT, GAME_WIDTH
import need, random, math

'''
###############################################################################
#OUTILS
###############################################################################
'''

def teamAdverse(teamid):
    adv=2
    if (teamid==2):
        adv=1
    return adv
            
'''            
class ContourneV3(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        adv = obstacle(state, teamid, player)
        if adv != None:
            me = player.position
            advd = obstacleD(state, teamid, player, adv)
            move = state.ball.position - player.position
            a = state.get_goal_center(need.teamAdverse(teamid))-player.position
            if adv.y<me.y:
                shoot = Vector2D.create_polar(a.shoot.angle + 0,45, 1)
            else:
                shoot = Vector2D.create_polar(a.shoot.angle - 0,45, 1)
                          
        return SoccerAction(move, shoot)
'''
'''import pdb
        pdb.set_trace()'''

'''
###############################################################################
#Stratégies sans ComposeStrat
###############################################################################
'''

###############################################################################
#Testeurs
###############################################################################
class Test(SoccerStrategy):
    def __init__(self):
        self.messi = Messi()
        self.fonce = Fonceur()
    def compute_strategy(self,state,player,teamid):
        ennemy = need.qqn_devant_moi(state,teamid,player)
        if ennemy == True:
            return self.messi.compute_strategy(state, player, teamid)
        else:
            return self.fonce.compute_strategy(state,player,teamid)
            


###############################################################################
#RANDOM
###############################################################################

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
        
###############################################################################
#Fonceur sans ComposeStrat
###############################################################################
      
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
        
###############################################################################
#Goal (useless)
###############################################################################

class Goal(SoccerStrategy):
    def __init__(self):
        self.name="Goal"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
            a=(state.ball.position+state.get_goal_center((teamid)))
            a.x=a.x/2.2
            a.y=a.y/2.2
            a=a-player.position
            shoot = Vector2D.create_polar(6,(teamid-1.5)*20)
            return SoccerAction(a,shoot) #Soit il tir a 10 soit a -10 en fonction de son équipe
    def copy(self):
        return Goal()
    def create_strategy(self):
        return Goal()   
        
###############################################################################
#Stratégie defensive
###############################################################################

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
        if d.norm > 30 :
            if (teamAdverse(teamid)==2):
                pos = Vector2D((0.2/5)*GAME_WIDTH,state.ball.position.y)-player.position
            else:
                pos = Vector2D((4.8/5)*GAME_WIDTH,state.ball.position.y)-player.position
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
        

       
      
class DefStratBis(SoccerStrategy):
    def __init__(self):
        self.name="DefStratBis"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        shoot = Vector2D(0,0)
        d = state.ball.position - player.position # diff entre ball et joueur
        
        if need.jai_la_balle(state,player)==False:
            if (teamAdverse(teamid)==2):
                pos = Vector2D((0.2/5)*GAME_WIDTH,state.ball.position.y)-player.position
            else:
                pos = Vector2D((4.8/5)*GAME_WIDTH,state.ball.position.y)-player.position
        else:
            pos= state.ball.position-player.position
            shoot= (state.get_goal_center(teamAdverse(teamid))-player.position)
        if need.jai_la_balle(state,player):
            
            shoot= (state.get_goal_center(teamAdverse(teamid))-player.position)
        print(shoot)
        return SoccerAction(pos,shoot)
    def copy(self):
        return DefStratBis()
    def create_strategy(self):
        return DefStratBis()
        
###############################################################################
#
###############################################################################

class Defenseur(SoccerStrategy):
    def __init__(self):
        self.name="Defenseur"
    def compute_strategy(self,state,player,teamid):
       
        g = state.get_goal_center(need.TeamMy(teamid))
        b = state.ball.position
        p = player.position
        gp = g-p
        bp = state.ball.position - player.position
        dist = b + g
        d = Vector2D((dist.x)/2.00,(dist.y)/2.00)   
        dirt = d - p
        dirt.product(10)
        if need.jai_la_balle(state,player) : 
            if b.y < GAME_HEIGHT/2.0:
                shoot2=Vector2D.create_polar(gp.angle + 2.505, 15)
                return SoccerAction(dirt,shoot2)
            else :
                shoot = Vector2D.create_polar(gp.angle - 2.505, 15)
                return SoccerAction (dirt,shoot)
        return SoccerAction(dirt,Vector2D())
    def create_strategy(self):
        return Defenseur() 
            
###############################################################################
#DefStratV2
###############################################################################

class DefStratV2(SoccerStrategy):
    def __init__(self):
        self.vasy = Messi()
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        shoot = Vector2D(0,0)
        d = state.ball.position - player.position # diff entre ball et joueur
        if d.norm > 25 :
            if (teamAdverse(teamid)==2):
                pos = Vector2D((1.3/5)*GAME_WIDTH,state.ball.position.y)-player.position
            else:
                pos = Vector2D((3.7/5)*GAME_WIDTH,state.ball.position.y)-player.position
        else:
            pos= state.ball.position-player.position
            shoot= (state.get_goal_center(teamAdverse(teamid))-player.position)
        if (PLAYER_RADIUS+BALL_RADIUS)>=(state.ball.position.distance(player.position)):
            return self.vasy.compute_strategy(state, player, teamid)
        return SoccerAction(pos,shoot)
    def copy(self):
        return DefStratV2()
    def create_strategy(self):
        return DefStratV2()

'''       
###############################################################################
#Stratégies de BASE
###############################################################################
'''        
###############################################################################
#Se déplace vers un point
###############################################################################

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
        
###############################################################################      
#Va vers la PELOTA
###############################################################################

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

###############################################################################
#Pour tirer vers le but adverse
###############################################################################

class Shoot(SoccerStrategy):
    def __init__(self):
        self.name="shoot"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        jai_la_balle = need.jai_la_balle(state,player)
        if jai_la_balle:
            shoot = state.get_goal_center(need.teamAdverse(teamid)) - player.position
            #print shoot.angle,shoot.create_polar(shoot.angle, 0.4)
            return SoccerAction(Vector2D(0,0), shoot.create_polar(shoot.angle, 1.8))
        return SoccerAction(Vector2D(0,0),Vector2D(0,0))
    def copy(self):
        return Shoot()
    def create_strategy(self):
        return Shoot()

###############################################################################
#Ne fais rien
###############################################################################

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

###############################################################################
#Contourne l'adversaire (Random)
###############################################################################

class Contourne(SoccerStrategy):
    def __init__(self):
        pass
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
            move = state.get_goal_center(need.teamAdverse(teamid))- (player.position)
            if need.jai_la_balle(state,player):
                shoot = Vector2D.create_polar(move.angle + random.random()*2-1,1)
                return SoccerAction(Vector2D(0,0), shoot)
            return SoccerAction(Vector2D(0,0), Vector2D())
    def create_strategy(self):
        return Contourne()

###############################################################################
#Countourne sans random (en fcontion de l'obstacle)
###############################################################################

class ContourneV2(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        adv = need.obstacle(state, teamid, player)
        me = player.position
        advD = need.obstacleD(state, teamid, player, adv)
        move = state.ball.position - player.position
        a = state.get_goal_center(need.teamAdverse(teamid))-player.position
        shoot = Vector2D(0,0)
        if adv:
            if adv.y<me.y:
                shoot = Vector2D.create_polar(a.angle + 0.45, 1)
            else:
                shoot = Vector2D.create_polar(a.angle - 0.5, 1)
        if advD == True:
            shoot= (state.get_goal_center(need.teamAdverse(teamid))-player.position)
                          
        return SoccerAction(move, shoot)

###############################################################################
#Tirer vers les potos
###############################################################################

class ShootPoto(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
            shoot = Vector2D(0,0)
            
            if need.jai_la_balle(state,player):
                shoot = state.get_goal_center(need.teamAdverse(teamid)) - player.position
                shoot.x = shoot.x - (GAME_GOAL_HEIGHT / 2.4)
                shoot.y = shoot.y - (GAME_GOAL_HEIGHT / 2.4)
            return SoccerAction(Vector2D(0,0), shoot)
      
class Test2(SoccerStrategy):
    def __init__(self):
        self.go = ComposeStrategy(GoToBall(),ShootPoto())
    def compute_strategy(self,state,player,teamid):
        return self.go.compute_strategy(state,player,teamid)
'''
###############################################################################
#Compositions de stratégies
###############################################################################
'''
        
###############################################################################
#Compose strat : go & shooter (BASE)
###############################################################################

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

        
###############################################################################
#GoToBall & Shoot 
###############################################################################

class Fonceur(SoccerStrategy):
    def __init__(self):
        self.name = Fonceur
        self.goball = ComposeStrategy(GoToBall(), Shoot())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return self.goball.compute_strategy(state, player, teamid)
        
###############################################################################
#Fonceur de poteaux 
###############################################################################

class FonceurPoto(SoccerStrategy):
    def __init__(self):
        self.go = ComposeStrategy(GoToBall(),ShootPoto())
    def compute_strategy(self,state,player,teamid):
        return self.go.compute_strategy(state,player,teamid)


###############################################################################
#Fonceur qui évite ses adversaires tout le temps
###############################################################################

class Evite(SoccerStrategy):
    def __init__(self):
        self.messi = ComposeStrategy(GoToBall(), Contourne())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return self.messi.compute_strategy(state, player, teamid)

###############################################################################
#Messi dribble SI ET SEULEMENT SI y a qqn devant lui !
###############################################################################

class Messi(SoccerStrategy):
    def __init__(self):
        self.name = Messi
        self.messi = Evite()
        self.fonce = Fonceur()
    def compute_strategy(self,state,player,teamid):
        ennemy = need.qqn_devant_moi(state,teamid,player)
        if ennemy == True:
            return self.messi.compute_strategy(state, player, teamid)
        else:
            return self.fonce.compute_strategy(state,player,teamid)
        
###############################################################################
#Defstrat en cas de besoin   ---> A BOSSER
###############################################################################

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
        if pos_ball.x > (GAME_WIDTH/2.8):
            return self.godef.compute_strategy(state, player, teamid)
        return self.goball.compute_strategy(state, player, teamid)
    def copy(self):
        return DefIntell()
    def create_strategy(self):
        return DefIntell()


    

###############################################################################
#Fonceur qui évite les joueurs
###############################################################################
'''
class Fon(SoccerStrategy):
    def __init__(self):
        self.goo = ComposeStrategy(GoToBall(), Shoot())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        #if ((PLAYER_RADIUS+BALL_RADIUS)) >= (state.ball.position.distance(player.position)):
        my_ball,player,distance = need.joueur_plus_proche(teamid, state)
        if my_ball == True :
            return self.goo.compute_strategy(state, player, teamid)
    def create_strategy(self):
        return Fon()
       
'''       
        
###############################################################################
#Dat player (myball = joueur plus proche de mon équipe .)
###############################################################################
#if pplayer == player #Si c moi le plus proche de la balle

class Dat(SoccerStrategy):
    def __init__(self):
        self.messi = Messi()
        self.fonce = Fonceur()
        self.godef = DefStrat()
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        joueurpp_mon_equipe,joueur_plus_proche,distance = need.joueur_plus_proche(teamid, state)
        mon_equipe_a_la_ball = need.mon_equipe_a_la_ball(teamid,state)
        if joueurpp_mon_equipe == False:
            return self.godef.compute_strategy(state, player, teamid)
        elif joueur_plus_proche == player and mon_equipe_a_la_ball:
            return self.fonce.compute_strategy(state, player, teamid)
        elif mon_equipe_a_la_ball:
            return self.fonce.compute_strategy(state,player,teamid)
        return self.godef.compute_strategy(state,player,teamid)
      
###############################################################################
#DefStrat pour 2v2 et 4v4 qui contourne en contre attaque
###############################################################################

class DefAttaque(SoccerStrategy):
    def __init__(self):
        self.defe = DefStrat()
        self.go = Messi
    def compute_strategy(self,state,player,teamid):
        ennemy = need.qqn_devant_moi(state,teamid,player)
        mon_equipe_a_la_ball = need.mon_equipe_a_la_ball(teamid,state)
        if mon_equipe_a_la_ball == True and ennemy == True:
            return self.go.compute_strategy(state,player,teamid)
        return self.defe.compute_strategy(state,player,teamid)
        
###############################################################################
# Messi tir vers les poteaux
###############################################################################
'''
class MessiP(SoccerStrategy):
    def __init__(self):
        self.messi = Messi()
        self.poto = FonceurPoto()
    def compute_strategy(self,state,player,teamid):
        ennemy = need.qqn_devant_moi(state,teamid,player)
        mon_equipe_a_la_ball = need.mon_equipe_a_la_ball(teamid,state)
        if ennemy == True and mon_equipe_a_la_ball == True:
            return self.messi.compute_strategy(state,player,teamid)
        return self.compute_strategy(state,player,teamid)'''
        
'''
###############################################################################
# IA
###############################################################################
#MixS pour def
###############################################################################
#SimpleSelector
###############################################################################

class SimpleSelector(SoccerStrategy):
    def __init__(self,list_strat):
        self.name="Selecteur simple"
        self.list_strat=list_strat
    def selector(self,state,player,teamid):
        if (...):
            return 0
        if (...):
            return 1
        return -1
        def compute_strategy(self,state,player,teamid):
            return self.list_strat[self.selector(state,player,teamid)]\.compute_strategy(...)
            
'''