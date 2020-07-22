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
        
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            portfolio.append(record)
            
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

''' Using prices from another file to calculate changes in prices of stock
    from portfolio '''
def make_report(portfolio, prices):
    table = []
    for s in portfolio:
        try:
            name = s['name']
            shares = int(s['shares'])
            price = float(s['price'])
            change = prices[name] - float(price)
            line = (name, shares, price, change)
            table.append(line)
        except KeyError:
            print('key is missing')
    return table

report = make_report(portfolio, prices)

#   Report Output 
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers)) 

for table in report:
    print('%10s %10d %10.2f %10.2f' % table)

''' Alternate Output '''
##for name, shares, price, change in report:
##    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
