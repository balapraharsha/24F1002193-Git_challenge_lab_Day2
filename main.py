import interest  

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid positive number!")

# Input with validation
principal = get_positive_float("Enter principal amount: ")
rate = get_positive_float("Enter annual interest rate (in %): ")
time = get_positive_float("Enter time in years: ")

si = interest.simple_interest(principal, rate, time)
total_amount = principal + si

print(f"\nSimple Interest: {si}")
print(f"Total Amount after {time} years: {total_amount}")

# Year-wise breakdown
print("\nYear-wise Breakdown:")
for year in range(1, int(time)+1):
    yearly_interest = interest.simple_interest(principal, rate, year)
    total = principal + yearly_interest
    print(f"Year {year}: Total Amount = {total}")
