# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    try:
        f = open(filename, 'rt')
    except FileNotFoundError:
        print(filename, 'can\'t be found, please provide a valid file')
    next(f).split(',')

    totalAmount = 0
    for line in f:
        row = line.split(',')
        try:
            totalAmount = totalAmount + (int(row[1]) * float(row[2]))
        except ValueError:
            print('Value not found for line', row, 'proceeding with remaining values in file')

    f.close()
    return totalAmount

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost is', cost)