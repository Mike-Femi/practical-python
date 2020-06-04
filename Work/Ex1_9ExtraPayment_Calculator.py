# Exercise 1.9: Making an Extra Payment Calculator.
# How much will Dave pay if he pays an extra $1000/month for 4 years
# starting in year 5 of the mortgage?



principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
while principal > 0:
    month = month + 1
    # Conditioning extra $1000 for 4 years after year 5
    if month >= 60 and month <= 108:
        payment = 3684.11
    else:
        payment = 2684.11
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid =',round(total_paid, 8))
print('Months =', month)
