#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:58:03 2024

@author: vishweshpalani
"""

import pandas as pd

init = {}

terminal_states = [(3,2)]
pitfalls = [(2,2)]

for x in range(1,4):
    for y in range(1, 3):
        state = (x, y)
        if state in terminal_states: init[state] = 20
        elif state in pitfalls: init[state] = -10
        else: init[state] = -1
        
upd = init.copy()
        
actions = [(0,1), (0,-1), (1,0), (-1,0)]

transition = {}

for a in actions:
    t = {}
    t[a] = 0.8
    for i in [1, -1]: 
        if a[0] == 0:
            t[(i, 0)] = 0.1
        else: 
            t[(0, i)] = 0.1
    transition[a] = t
    
        

        
#checks and multiplies the state with the probabiliity
def move(util_state, coord, move, prob):
    new_state = (coord[0] + move[0], coord[1] + move[1])
    if new_state not in util_state: return util_state[coord] * prob
    return util_state[new_state] * prob

#result of a single action
def action(util_state, coord, a):
    t = transition[a]
    util = 0
    for m in t:
        util += move(util_state, coord, m, t[m])
    return util
    
#new utility
def util(init, util_state, coord, discount):
    utils = []
    for a in actions:
       utils.append(action(util_state, coord, a))
    return init[coord] + discount * max(utils)


def update(init, util_state, discount):
    new_util = {}
    for s in util_state:
        if s in terminal_states:
            new_util[s] = util_state[s]
        else:
            new_util[s] = util(init, util_state, s, discount)
    return new_util

def print_state(util_state, x_limit, y_limit):
    table = []
    for y in range(1, y_limit + 1):
        row = []
        for x in range(1, x_limit + 1):
            row.append(util_state[(x, y_limit + 1 - y)])
        table.append(row)
        
    df = pd.DataFrame(table, columns = ['1', '2', '3'], index=['2', '1'])
    print(df)

num_iters = 10
discount = 0.8

print_state(upd, 3, 2)
    
for i in range(num_iters):
    upd = update(init, upd, discount)
    print_state(upd, 3, 2)
            
    
    