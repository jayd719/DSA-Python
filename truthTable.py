from itertools import product

s = [True,False]

outcomes = [outcome for outcome in product(s,s,s,s,s,s)]
