# 9.5 Challenge: Wax Poetic

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

# Randonly select text from lists based on the type and number passed in
def collector(type, iterations):
    import random

    random_elements = []

    num_nouns = 0
    while num_nouns < iterations:
        random_elements.append(random.choice(type)) 
        num_nouns = num_nouns + 1
    
    if (type == adverbs):
        random_elements = random_elements.pop()
    return random_elements

# nouns = [random_generator(), random_generator(), random_generator()] 

noun1, noun2, noun3 = collector(nouns, 3)
verb1, verb2, verb3 = collector(verbs, 3)
adj1, adj2, adj3 = collector(adjectives, 3)
prep1, prep2 = collector(prepositions, 2)
adverb1 = collector(adverbs, 1)
# test1 = collector(nouns, 2)

if (adj1 == "incredulous") or (adj1 == "exuberant"):
    start = "An"
else:
    start = "A"

# poem
# start should be A/An
# first 3 subs (start, adj1, noun1) are the same on both lines
print(f"{start} {adj1} {noun1}")
print()
print(f"{start} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}")
print(f"{adverb1}, the {noun1} {verb2}")
print(f"the {noun2} {verb3} {prep2} a {adj3} {noun3}")     
print()

