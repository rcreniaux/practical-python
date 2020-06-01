# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    f = open(filename)
    rows = csv.reader(f)
    # skipping headers
    next(rows)

    totalAmount = 0
    for row in rows:
        try:
            totalAmount = totalAmount + (int(row[1]) * float(row[2]))
        except ValueError:
            print('Value not found for line', row, 'proceeding with remaining values in file')

    f.close()
    return totalAmount


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    
cost = portfolio_cost(filename)
print('Total cost is', cost)