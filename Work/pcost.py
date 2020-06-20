# pcost.py
#
# Exercise 1.27

# changing work directory
'''import os  
os.chdir('C:\\Users\\Mike-Femi\\Desktop\\practical-python\\Work')

cost = 0.0
total_cost = 0.0
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)           # computer isolates the header row and moves to the next
    print(' Stock', '    cost') # New header for output
    for line in f:
        row = line.split(',')
        name = row[0]
        nshares = int(row[1])
        price = float(row[2])
        cost = nshares * price
        total_cost += nshares * price   
        print(f'{name:>6} = {cost:08.2f}')

print('Total cost is', total_cost)

'''

#import os
# os.chdir('C:/Users/Mike-Femi/Desktop/practical-python/Work')
###########  HANDLING ERRORS  ###################
'''

def portfolio_cost(filename):
    cost = 0.0
    total_cost = 0.0
    with open(filename, 'rt') as f:
        headers = next(f)
        print(' Stock', '    cost')
        for line in f:
            row = line.split(',')
            try:
                name = row[0]
                nshares = int(row[1])
                price = float(row[2])
                cost = nshares * price
                total_cost += nshares * price
                print(f'{name:>6} = {cost:08.2f}')
            except ValueError:
                print("Couldn't parse", line)
    print('Total cost is', total_cost)
'''
############################################################


#  USING A LIBRARY FUNCTION: (import csv)
'''
import csv
def portfolio_cost(filename):
    cost = 0.0
    total_cost = 0.0
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    print(' Stock', '    cost')
    for row in rows:
        #row = line.split(',') line of code is now unnecessary with import csv
        try:
            name = row[0]
            nshares = int(row[1])
            price = float(row[2])
            cost = nshares * price
            total_cost += nshares * price
            print(f'{name:>6} = {cost:08.2f}')
        except ValueError:
            print("Couldn't parse", row)
    print('Total cost is', total_cost)
'''



import os
os.chdir('C:/Users/Mike-Femi/Desktop/practical-python/Work')
import sys
import csv
def portfolio_cost(filename):
    cost = 0.0
    total_cost = 0.0
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    print(' Stock', '    cost')
    for row in rows:
        try:
            name = row[0]
            nshares = int(row[1])
            price = float(row[2])
            cost = nshares * price
            total_cost += nshares * price
            print(f'{name:>6} = {cost:08.2f}')
        except ValueError:
            print("Couldn't parse", row)
    print('Total cost is', total_cost)
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
