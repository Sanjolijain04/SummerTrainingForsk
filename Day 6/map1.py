# using map and lambda
#import library for randomness
import random


names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

replaced=list(map(lambda name: random.choice(code_names), names))
print(replaced)