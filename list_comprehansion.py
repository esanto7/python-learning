breakfast = ["eggs", "fruit", "orange juice"]

print("The items in the list are: eggs, fruit, orange juice")
print("Getting the lengths of the items via a list comprehension...")
lengths = [len(item) for item in breakfast]

print(lengths[0:])
