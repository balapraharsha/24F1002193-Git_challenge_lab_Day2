import interest

print("Simple Interest Calculator")

principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (in %): "))
time = float(input("Enter time in years: "))

si = interest.simple_interest(principal, rate, time)
total_amount = principal + si

print(f"\nSimple Interest: {si}")
print(f"Total Amount after {time} years: {total_amount}")
