#Richard Hopkins
#ProgrammingFundamentals 9/8
#acreageCalc

#input
width = float(input("Enter the width in feet: "))
length = float(input("Enter the length in feet: "))

#acreage formula
acre = width * length / 43560


#output
print(format('The acreage is'), format(acre, '.2f'), 'acres.')
