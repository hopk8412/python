#Richard Hopkins
#Programming Fundamentals
#9/15/2016

#userInput

while True:
    try:
        numPack = int(input("Enter the number of packages you're buying: "))
    except ValueError:
        print("You can only order whole packages...")
        continue
    else:
        break
    
#multiplier

if numPack >= 100:
    multi = 0.40

elif numPack >= 50 and numPack <= 99:
    multi = 0.30

elif numPack >= 20 and numPack <= 49:
    multi = 0.20

elif numPack >=10 and numPack <= 19:
    multi = 0.10

elif numPack < 10 and numPack > 0:
    multi = 0.00
   
#formulas
    
cost = numPack * 99
discount = cost * multi
total = cost - discount

#output
    
if discount <= 0.00:
    print(format('Your price is', '20s'), '$', format(total, '15,.2f'))

else:
    print(format('Your discount is', '20s'), '$', format(discount, '15,.2f'))
    print(format('Your price is', '20s'), '$', format(total, '15,.2f'))
    
