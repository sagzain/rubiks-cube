#!/usr/bin/python3
# -*- coding: utf-8 -*-

from JsonManager import JsonManager as jManager
from TreeNode import TreeNode
from State import State
from pprint import pprint

class StateSpace:
    def __init__(self, json):
        self.path = json
        self.json = jManager.jsonReading(self.path)

    def successors(self, state, depth, x):
        nodes = []
        if depth == x:
            return []
        else:
            for move in state.current.validMovements():
                method = getattr(state.current.clone(), move[0])
                print(method)
                print("method: ",state.md5)
                method(int(move[1]))
                newState = State(state.current)
                print("new: ",newState.md5)
                pprint(newState.current.faces)
                print("movement: ", move, "\n")
                acc = move
                costAct = 1
                nodes.append((acc, newState, costAct))
            return nodes
