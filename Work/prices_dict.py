import os
os.chdir('C:/Users/Mike-Femi/Desktop/practical-python/Work')

''' Mapping names to prices from a file '''
import csv

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
