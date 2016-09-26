# Richard Hopkins

#input
milesStr = input("Enter the miles driven: ")
miles = float(milesStr)

gallons = float(input("Enter the number of gallons of gas: "))

#processing
mpg = miles / gallons
answer = format(mpg, ".1f")

#output
print ("The MPG rating was", answer, "miles per gallon.")
print("mpg is still", mpg)

#wait in command prompt until user presses enter or closes window
needInput = input("Press enter to exit...")
