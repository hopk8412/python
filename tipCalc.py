food = float(input('Enter the amount of the food: '))
tax = food * 0.07
tip = food * 0.18
total = food + tax + tip

print(format('Cost of food', '20s'), '$', format(food, "10,.2f"))
print(format('Tax', '20s'), '$', format(tax, "10,.2f"))
print(format('Tip', '20s'), '$', format(tip, "10,.2f"))
print(format('Total cost', '20s'), '$', format(total, "10,.2f"))
