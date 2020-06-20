cost = 0.0
total_cost = 0.0
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)           # computer isolates the header row and moves to the next
    #print(' Stock', '    cost') # New header for output
    for line in f:
        fields = line.split(',')
        try:
            shares = int(fields[1])
        except ValueError:
            print("Couldn't parse", line)
        print(shares)
        '''name = row[0]
        nshares = int(row[1])
        price = float(row[2])
        cost = nshares * price
        total_cost += nshares * price   
        print(f'{name:>6} = {cost:08.2f}')'''

#print('Total cost is', total_cost)
