# fileparse.py
#
# Exercise 3.3

import os
os.chdir('C:/Users/Mike-Femi/Desktop/practical-python/Work')

import csv
from pprint import pprint
def parse_csv(filename, select = None, types = None, has_headers=None, delimiter=None):
    '''
    Parse a csv file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter =' ')

        # Read the file headers
        if has_headers == True:
            headers = next(rows)
        
            # If a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []
            
            records = []
            for row in rows:
                if not row:   # Skip row with no data
                    continue
                # Filter the row if specific columns were selected
                if indices:
                    row = [ row[index] for index in indices ]
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                # Make a dictionary
                record = dict(zip(headers, row))
                records.append(record)
        else: # in case file does not contain headers
            records = []
            for row in rows:
                if not row:
                    continue
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                header = ('Name', 'price')
                record = dict(zip(header, row))    
                records.append(record)

    return records
