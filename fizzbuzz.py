for num in range(0,101):
    if not(num % 5) and not(num % 3):
        print("FizzBuzz")
    elif not(num % 3):
        print("Fizz")
    elif not(num % 5):
        print("Buzz")
    else:
        print(num)
