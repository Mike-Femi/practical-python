# timethis.py

import time

def timethis(func):
    '''
    Wraps a function with an extra layer of logic that prints
    out how long it takes for a function to execute
    '''
    def wrapper(*args,**kwargs):
        start = time.time()
        try:
            return func(*args,**kwargs)
        finally:
            end = time.time()
            print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
    return wrapper

'''
This @timethis decorator can be placed in front of any function definition.
Thus, you might use it as a diagnostic tool for performance tuning.
'''
if __name__ == '__main__':
    @timethis
    def countdown(n):
        while n > 0:
            n-= 1

    countdown(1000000)
