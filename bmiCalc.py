#Richard Hopkins
#Programming Fundamentals
#9/15/2016

#input

weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

#formula

BMI = weight * 703 / height ** 2

#booleans and output

if 18.5 <= BMI <= 25:
    print("BMI is", format(BMI, '.1f'))
    print("This is considered optimal.")
    
elif BMI < 18.5:
    print("BMI is", format(BMI, '.1f'))
    print("This is considered underweight.")

elif BMI > 25:
    print("BMI is", format(BMI, '.1f'))
    print("This is considered overweight.")
    
