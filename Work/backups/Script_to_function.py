import os
os.chdir('C:/Users/Mike-Femi/Desktop/practical-python/Work')


def portfolio_cost(filename):
    cost = 0.0
    total_cost = 0.0
    with open(filename, 'rt') as f:
        headers = next(f)
        print(' Stock', '    cost')
        for line in f:
            row = line.split(',')
            name = row[0]
            nshares = int(row[1])
            price = float(row[2])
            cost = nshares * price
            total_cost += nshares * price
            print(f'{name:>6} = {cost:08.2f}')
    print('Total cost is', total_cost)
