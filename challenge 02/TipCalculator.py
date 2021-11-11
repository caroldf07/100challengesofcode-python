# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print("Hey There! Let's split this bill 📈\n")
bill = float(input("What was the total bill? $"))
people = int(input("How many people? "))
tip = float(input("And the tip is? "))

total_per_person = (bill/people)*(1 + (tip/100))

print(f"Each person should pay ${total_per_person:.2f}")
