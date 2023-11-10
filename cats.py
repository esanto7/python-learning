# cats
# 1 = Hat; 0 = No Hat
cats = {}

i = 1
c = 1 # counts cats
d = 2 # tracks the counter / divisor

while i <= 100:
    cats[i] = {"cat_" + str(i): 1}
    i = i + 1

# print(cats)

for x in cats:
    for c in cats:
        if c % d == 0:
            cats[c] = 0
    d = d + 1

print(cats)