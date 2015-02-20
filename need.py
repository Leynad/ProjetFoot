# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 15:20:23 2015

for p in state.team1/2.player
"""

import math

###############################################################################
#ID de la TEAM
###############################################################################

def teamAdverse(id):
    if (id == 1):
        return 2
    else:
        return 1
        
''' def myBall(id,state):
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
        return(dmin) '''

###############################################################################
# My ball ? player ? distance ?
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

'''
####
#+
###        

def pos_ball(id, state):
    return self.state.ball.position

def pos_player(id,state):
    return self.state.player.position
'''
    
'''    
dt1 = min(pos_ball.distance( state.team1.players ))
    dt2 = min()
    if(pos_ball.distance(player.position)) <= (BALL_RADIUS + PLAYER_RADIUS):
    
'''
    