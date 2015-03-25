from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pickle
import os
from soccersimulator import TreeIA, TreeStrategy
from td1 import *

def gen_feature_simple(state,teamid,playerid):
    return np.array([f(state,teamid,playerid) for f in list_fun_features])
    
def distance_ball(state,teamid,playerid):
    return (state.get_team(teamid)[playerid].position-state.ball.position).norm

def distance_mon_but(state,teamid,playerid):
    return (state.get_goal_center(teamid)-state.get_team(teamid)[playerid].position).norm

def distance_autre_but(state,teamid,playerid):
    return (state.get_goal_center(3-teamid)-state.get_team(teamid)[playerid].position).norm

def distance_ball_mon_but(state,teamid,playerid):
    return (state.get_goal_center(teamid)-state.ball.position).norm


def distance_ball_autre_but(state,teamid,playerid):
    return (state.get_goal_center(3-teamid)-state.ball.position).norm
    
list_fun_features=[distance_ball_mon_but]

def gen_feature_simple(state,teamid,playerid):
    return np.array([f(state,teamid,playerid) for f in list_fun_features])
    
if __name__=="__main__":
    treeia=TreeIA(gen_feature_simple)
    treeia.learn(fn="best_goal")
    treeia.save("best_goal.pkl")
    treeia.to_dot("best_goal.dot")