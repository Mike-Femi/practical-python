# closure.py
'''
Example on using Closure and Delayed Evaluation
'''
import time

def add(x, y):
    def do_add(): # closure
        print(f'Adding {x} + {y} -> {x+y}')
    return do_add

def after(seconds, func): # To delay evaluation
    time.sleep(seconds)
    func()

after(30, add(2, 3))
# `do_add` has the references x -> 2 and y -> 3
