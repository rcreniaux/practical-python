# pcost.py
#
# Exercise 1.27
f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')

totalAmount = 0

for line in f:
    row = line.split(',')
    totalAmount = totalAmount + (int(row[1]) * float(row[2]))

f.close()

print('Total cost is', totalAmount)