word = input("Enter a word: ")
print("Comparing your word to the number 5...")

if (len(word) < 5):
    print(f"Your input is less than 5 characters long.")
elif (len(word) == 5):
    print("Your input is 5 characters long.")
else:
    print("Your input is greater than 5 characters long.")
