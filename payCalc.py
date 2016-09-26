hours = float(input("Enter the hours worked: "))
rate = float(input("Enter the hourly rate: "))

pay = hours * rate

if hours > 40:
    overtime = hours - 40
    normalpay = 40 * rate
    otpay = overtime * rate * 1.5
    pay = normalpay + otpay

else:
    pay = hours * rate

print("Pay earned was $", format(pay, ".2f"))
