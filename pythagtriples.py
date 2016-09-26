a = int(input("Enter the length of one side of your triangle: "))
b = int(input("Enter another length of the triangle: "))
c = int(input("Enter the last length of your triangle: "))


if a ^ 2 + b ^ 2 == c ^ 2:
    print("This is a Pythagorean triple!")
else:
    print("This is NOT a Pythagorean triple!")
        
