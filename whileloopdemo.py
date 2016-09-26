#count is employees already processed
count = 0
total = 0
numEmployees = int(input("How many employees worked this week? "))

while count < numEmployees:
    name = input("Enter the name for employee #"+str(count + 1) + ": ")
    hours = float(input("Enter the hours: "))
    rate = float(input("Enter the hourly rate: "))

    if hours > 40:
        pay = 40 * rate + (hours - 40) * 1.5 * rate
    else:
        pay = hours * rate

    total += pay
    print("Pay earned by", name, "was $", format(pay, ",.2f"))

    count += 1

print("Total payroll was $", format(total, ",.2f"))
