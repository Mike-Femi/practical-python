# report.py
#
# Exercise 2.4

from . import tableformat
from . import fileparse
from .stock import Stock
from .portfolio import Portfolio

def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        return Portfolio.from_csv(lines, **opts)

def read_prices(filename):
    '''
    Read prices from a CSV file of name,price data
    '''      
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines,types=[str,float], has_headers=False))

def make_report(portfolio, prices):
    '''
    This tabulates the result

    '''
    table = []
    for s in portfolio:
        row = (s.name, s.shares, prices[s.name], prices[s.name] - s.price)
        table.append(row)
    return table


def print_report(report, formatter):
    '''
    This function prints the required output
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make stock report from given files (portfolio and prices)
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Call the tabular report function
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
'''
    formatter = tableformat.TextTableFormatter()
    print_report(report, formatter)
'''
def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfoliofile pricefile format' % args[0])
    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)
#portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
