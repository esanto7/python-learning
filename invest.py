def invest (amount, rate, years):
    amount = int(amount) * (1 + float(rate))
    return amount

initial = float(input("Enter an initial amount: "))
percent = input("Enter an annual percentage: ")
num_years = int(input("Enter a number of years: "))

for i in range(0, num_years):
    initial = invest(initial, percent, num_years)
    print(f"Year {i + 1}: ${initial:.2f}")
    

