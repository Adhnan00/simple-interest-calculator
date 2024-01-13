# simple_interest.py

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a decimal): "))
time = float(input("Enter the time the money is invested or borrowed for (in years): "))

simple_interest = principal * rate * time

print(f"Simple Interest: {simple_interest}")
