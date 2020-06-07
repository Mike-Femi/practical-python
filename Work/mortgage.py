# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
while principal > 0:
    month = month + 1
# Conditioning extra $1000 payment for 4 years after year 5
    if month >= 60 and month <= 108:
        payment = 3684.11
    else:
        payment = 2684.11
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    '''print(month, round(total_paid, 2), round(principal, 2))'''


# Exercise 1.17: Using f-strings for the output    
    print(f'{month:4d} {total_paid:10.2f} {principal:10.2f}')


'''
print('Total paid =',round(total_paid, 5))
print('Months =', month)
'''



print(f'Total paid = {total_paid:0.2f} in {month} months')
