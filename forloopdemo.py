numEmployees = int(input("how many empoloyees worked this week? "))
total = 0

for count in range(numEmployees):
    name = input("Enter the name for employee #"+str(count + 1) + ": ")
    hours = float(input("Enter the hours: "))
    rate = float(input("Enter the hourly rate: "))

    if hours > 40:
        pay = 40 * rate + (hours - 40) * 1.5 * rate
    else:
        pay = hours * rate

    total += pay
    print("Pay earned by", name, "was $", format(pay, ",.2f"))


print("Total payroll was $", format(total, ",.2f"))
