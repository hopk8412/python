per = float(input("What was the percentage? "))

if 90 <= per:
    grade = "A"
elif 80 <= per:
        grade = "B"
elif 70 <= per:
            grade = "C"
elif 60 <= per:
                    grade = "D"
else:
    grade = "F"

print("The letter grade for", per, "% is",grade)
