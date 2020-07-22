# report.py
#
# Exercise 2.4


import os  # Changing current working directory
os.chdir('C:/Users/Mike-Femi/Desktop/practical-python/Work')

import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            stock = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append(stock)
            
    return portfolio



def read_prices(filename):
    '''
    Read prices from a CSV file of name,price data
    '''
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


def make_report(portfolio, prices):
    '''
    This tabulates the result

    '''
    table = []
    for s in portfolio:
        row = (s['name'], s['shares'], prices[s['name']], prices[s['name']] - s['price'])
        table.append(row)
    return table


def print_report(report):
    '''
    This function prints the required output
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for table in report:
        print('%10s %10d %10.2f %10.2f' % table)


def portfolio_report(portfolio_filename, prices_filename):
    '''
    Make stock report
    '''
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Call the tabular report function
    report = make_report(portfolio, prices)

    # Call the print out function
    print_report(report)

#portfolio_report('Data/portfolio.csv', 'Data/prices.csv')






#portfolio_report('Data/portfolio2.csv', 'Data/prices.csv')

files = ['Data/portfolio.csv', 'Data/portfolio2.csv']

for name in files:
	print(f'{name:-^43s}')
	portfolio_report(name, 'Data/prices.csv')
	print()
