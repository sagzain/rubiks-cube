#!/usr/bin/python3
#-*- coding: utf-8 -*-

import Main
from Cube import Cube
from pprint import pprint

def start():
    cube = Cube(Main.jsonReading())
    menu(cube)

def menu(cube):
    while True:
        selection = 0
        try: selection = int(input("Options for testing:\n\t1 - Test a move\n\t2 - Test every movement\nSelection:")) 
        except ValueError:
            print("Error, selection must be integer")
            continue
        if selection == 1:
            testOneMove(cube)
            break
        if selection == 2:
            testingBackFront(cube)
            break
        else: print("Not a valid selection")

def testOneMove(cube):
    moves = ["B0", "B1", "B2", "b0", "b1", "b2"]
    while True:
        key = 0
        try: key = input("Select move type B0/B1/B2 (90º) or b0/b1/b2 (-90º):")
        except ValueError:
            print("Error, selection must be integer")
            continue
        if key in moves:
            if list(key)[0] == 'b':
                cube.b(int(list(key)[1]))
            else:
                cube.B(int(list(key)[1]))
            break
        else:
            print("Not a valid selection")
            
def testingBackFront(cube):
    for n in range(3):
        print("Aplying B%d movement" %n)
        cube.B(n)
        pprint(cube.Faces)
                
    for n in range(3):
        print("Aplying b%d movement" %n)
        cube.b(n)
        pprint(cube.Faces)
           
if __name__ == '__main__':
    start()
    
    
