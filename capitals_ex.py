capitals_dict = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas' : 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
}

import random

state, capital = random.choice(list(capitals_dict.items()))

# = output

print(f"The state is {state}")
# print(capital)

user_input = ""

while user_input.lower() != capitals_dict[state].lower():
    user_input = input("Enter the capital: ")
    if (user_input == "exit"):
        break

if (user_input.lower() == capitals_dict[state].lower()):
    print("Correct!")
else:
    print(f"The correct answer is: {capitals_dict[state]}")
    print("Goodbye.")
    
