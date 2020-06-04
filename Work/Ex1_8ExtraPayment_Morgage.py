# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0 # introduced new variable 'month'
while principal > 0:
    month = month + 1
    # Conditioning extra $1000 for the first 12 months
    if month <= 12:
        payment = 3684.11
    else:
        payment = 2684.11
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid =',round(total_paid, 8))
print('Months =', month)
