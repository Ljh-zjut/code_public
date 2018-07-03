#! usr/bin/env python3
# -*- coding: utf-8 -*-

state = [i for i in range(16)]

#initial values
values =  [0 for _ in range(16)]

# action
actions = ["n","e","s","w"]

#use a dictionary for convenient computation of next state id
#执行行为后到下一个状态的id改变量
ds_actions = {"n": -4, "e": 1, "s": 4, "w": -1}

#discount factor
gamma = 1.00

# 根据当前状态和采取的行为计算下一个状态id以及得到的即时奖励

def nextStates(s,a):
    next_state = s
    if (s%4 == 0 and a=="w") or (s<4 and a == "n") or ((s+1)%4 == 0 and a == "e") or (s > 11 and a == "s"):
        pass
    else:
        ds = ds_actions[a]
        next_state = s + ds
    return next_state