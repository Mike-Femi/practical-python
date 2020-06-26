import os
os.chdir('C:/Users/Mike-Femi/Desktop/practical-python/Work')

import csv

def push(filename):
    pf = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            hd = (row[0], int(row[1]), float(row[2]))
            pf.append(hd)
    return pf
