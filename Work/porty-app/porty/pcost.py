# pcost.py
#
# Exercise 1.27




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
    for rowno, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            name = record['name']
            nshares = int(record['shares'])
            price = float(record['price'])
            cost = nshares * price
            total_cost += nshares * price
            print(f'{name:>6} = {cost:08.2f}')
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')
    print('Total cost is', total_cost)
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
'''


from . import report

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print('Total cost = ', portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)
