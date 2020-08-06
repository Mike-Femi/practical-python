# stock.py

from typedproperty import String, Integer, Float

class Stock:
    name = String('name')  # String = lambda name: typedproperty(name, str)
    shares = Integer('shares') # Integer = lambda name: typedproperty(name, int)
    price = Float('price')
    '''
    An instance of a stock holding consisting of name, shares and price
    '''
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
    @property
    def cost(self):
        '''
        Return cost by : shares x price
        '''
        return self.shares * self.price
    
    def sell(self,amt):
        '''
        Sell a number of shares
        '''
        self.shares -= amt
