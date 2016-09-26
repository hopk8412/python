#Richard Hopkins
#Programming Fundamentals 9/8
#Sales Tax


#input
amount = float(input('Enter the amount of the purchase: '))

#tax rates
stateTax = amount * 0.05
countyTax = amount * 0.025

#Total of taxes, total of sale
totalTax = stateTax + countyTax
totalSale = amount + totalTax


#output
print(format('Amount of purchase', '20s'), '$', format(amount, '15,.2f'))
print(format('State sales tax', '20s'), '$', format(stateTax, '15,.2f'))
print(format('County sales tax', '20s'), '$', format(countyTax, '15,.2f'))
print(format('Total sales tax', '20s'), '$', format(totalTax, '15,.2f'))
print(format('Total of sale', '20s'), '$', format(totalSale, '15,.2f'))
