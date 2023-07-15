num = input("Enter a number less than 20: ")

for i in range(1, int(num) + 1):
    if (int(num) % i == 0):
        print(f"{i} is a factor of {num}")
