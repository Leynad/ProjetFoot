# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 15:20:23 2015

for p in state.team1/2.player
"""
from td1 import *


###############################################################################
#ID de la TEAM
###############################################################################

def teamAdverse(id):
    if (id == 1):
        return 2
    else:
        return 1

###############################################################################
#My ball ? player ? distance ?
###############################################################################

def joueur_plus_proche(id, state):
    pos_ball = state.ball.position
    def get_second(p):
        return p[1]
    p1, d1 = min(((p, pos_ball.distance(p.position)) for p in state.team1.players),
                 key = get_second)
    p2, d2 = min(((p, pos_ball.distance(p.position)) for p in state.team2.players),
                 key = get_second)
    if d1<d2:
        pproche=p1
        dproche=d1
    else:
        pproche=p2
        dproche=d2
    mon_equipe_est_proche = id==1 and d1<d2 or id==2 and d1>d2
    return (mon_equipe_est_proche, pproche, dproche)
    
###############################################################################
#Est-ce que j'ai la balle ?
###############################################################################

def mon_equipe_a_la_ball(id,state):
    mon_equipe_est_proche, pproche, dproche = joueur_plus_proche(id, state)
    return mon_equipe_est_proche and dproche < (BALL_RADIUS+PLAYER_RADIUS)/2
                                   
 
###############################################################################
#Obstacle 
####"##########################################################################

def obstacle(state, teamid, player): 
    teamadv = teamAdverse(teamid)
    coord = None
    if (teamadv==1):
        list_joueurs = state.team2.players
    else:
        list_joueurs = state.team1.players
    for p in list_joueurs:
        if (p.position.distance(player.position) < (GAME_WIDTH*0.2) ) :
            coord = p.position
            return coord
            
###############################################################################
#Ou est le l'obstacle ?
###############################################################################

def obstacleD(state, teamid, player, adv):
    teamadv = teamAdverse(teamid)
    me = player.position
    a = False
    if (adv!=None):
        if (teamadv==1):
            if(adv.x > me.x):
                a = True
            else:
                a = False
        else:
            if(adv.x<me.x):
                a = True
            else:
                a = False                
    return a 

###############################################################################
#Obstacle V2 
###############################################################################

def qqn_devant_moi(state,teamid,player):
    if teamid == 1:
        list_adv = state.team2.players
    else:
        list_adv = state.team1.players
    progression = state.get_goal_center(teamAdverse(teamid))-state.get_goal_center(teamid)
    for p in list_adv:
        d=p.position - player.position
        if d.dot(progression)>0:
        #if abs(d.angle(progession)>math.pi/4:
            if d.norm<(BALL_RADIUS+PLAYER_RADIUS)*35:
                return True
    return False
    
'''
###############################################################################
#Pour la lisibilité du code
###############################################################################        

def pos_ball(state):
    return state.ball.position

def pos_player(state):
    return state.player.position
    
    
    


###############################################################################
#Brouillon
###############################################################################    
    
def myBall(id,state):
    pos_ball=state.ball.position
    list1 = state.team1.players  # liste des joueurs de la team 1   
    dmin = 1000
    imin = -1    
    res = [pos_ball.distance(p.position) for p in list1]
    dmin1= min(res)
    idx_p1 = res.index(dmin1)
    if dmin < pos_ball.distance(p.position):
        dmin = pos_ball.distance
        return(dmin)
    
    
            
    list2 = state.team1.players #liste des joueurs de la team 2
    res2 = [pos_ball.distance(p.position) for p in list2]
    idx_p2 = res.index(dmin)
    dmin2 = min(res2)
    if dmin < pos_ball.distance(p.position):
        dmin = pos_ball.distance
        return(dmin) 
    
    
    
dt1 = min(pos_ball.distance( state.team1.players ))
    dt2 = min()
    if(pos_ball.distance(player.position)) <= (BALL_RADIUS + PLAYER_RADIUS):
'''