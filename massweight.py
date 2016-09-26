#Richard Hopkins
#Programming Fundamentals
#9/15/2016

#input

mass = float(input("Enter the mass in kilograms: "))
weight = float(mass * 9.8)

#output

print("Weight is", format(weight, '.1f'), "newtons.")

#boolean

if weight > 500:
    print("WARNING: WEIGHT IS TOO HIGH!")

elif weight < 100:
    print("WARNING: WEIGHT IS TOO LOW!")
