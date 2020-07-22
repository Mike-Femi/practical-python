# fileparse.py
#
# Exercise 3.3

import os
os.chdir('C:/Users/Mike-Femi/Desktop/practical-python/Work')

import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a csv file into a list of records with type conversion.
    '''
    rows = csv.reader(lines, delimiter=delimiter)
    
    # Raising exception for arguments' conflict
    if select and has_headers==False:
        raise RuntimeError(" select argument requires column headers")
    elif silence_errors==True:
        pass
    # Read the file headers if it exists 
    headers = next(rows) if has_headers else []

    # if specific columns have been selected, make indices for filtering

    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    
    records = []
    for rowno, row in enumerate(rows, start=1):
        try: # To Catch all value errors
            
            if not row:   # Skip row with no data
                continue
            # Filter the row if specific columns were selected
            if select:
                row = [ row[index] for index in indices ]
            #  Apply type conversion to the row
            if types:
                row = [func(val) for func, val in zip(types, row)]
            # Make a dictionary or a tuple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        except ValueError as e:
            if silence_errors==True:
                pass
            else:
                print(f'Row {rowno}: Couldn\'t convert {row}')
                print(f'Row {rowno}: Reason {e}')
            
    return records
'''
def main(args):
    if len(args) < 2:
        raise SystemExit("Usage: ' lines = open('filename', 'rt')")
        raise SystemExit("port = fileparse.parse_csv(lines, args[1] ....args[n])")
    parse_csv()

if __name__ == '__main__':
    import sys
    main(sys.argv)
'''
