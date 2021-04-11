def solve(meal_cost, tip_percent, tax_percent):
    tip = (tip_percent / 100) * meal_cost
    print('Total tip = ', round(tip, 2))
    print('Total tip = ', tip)
    tax = (tax_percent / 100) * meal_cost
    print('Total tax = ', round(tax, 2))
    print('Total tax = ', tax)
    total_cost = meal_cost + tip + tax
    print('Total Cost: ', round(total_cost,2))
    print("{:.2f}".format(round(total_cost, 2)))


if __name__ == '__main__':
    meal_cost = float(input('Meal cost: '))
    tip_percent = int(input('Tip: '))
    tax_percent = int(input('Tax: '))
    solve(meal_cost, tip_percent, tax_percent)
