# report.py
#
# Exercise 2.4

'''Changing current working directory'''
import os
os.chdir('C:/Users/Mike-Femi/Desktop/practical-python/Work')

'''Reading a stock portfolio into a list of dictionaries'''

import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            # holding = (row[0], int(row[1]), float(row[2]))
            stock = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(stock)
            
    return portfolio


''' Mapping names to prices from a csv file '''


def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                
                prices[str(row[0])] = float(row[1])
            except IndexError:
                pass
            
    return prices

# Running the functions.....
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

''' Calculating total cost of portfolio '''
total_cost = 0.0
for s in portfolio:
    total_cost += s['shares'] * s['price']
print('Total cost =', total_cost)

''' Calculating current value of portfolio '''
current_value = 0.0
for s in portfolio:
    current_value += s['shares'] * prices[s['name']]
print('Current value =', current_value)

''' Calculating gain/loss of the portfolio '''
loss = 0.0
gain = 0.0
if total_cost > current_value:
    loss = total_cost - current_value
    print('Loss =', loss)
else:
    gain = current_value - total_cost
    print('Gain =', gain)
