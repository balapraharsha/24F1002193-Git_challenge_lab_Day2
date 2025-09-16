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
