# pcost.py
#
# Exercise 1.27
import csv

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

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost is', cost)