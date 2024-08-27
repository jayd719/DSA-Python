import itertools

ranks = [str(rank) for rank in list(range(2,11))+["J","Q","K","A"]]
suits = ["hearts","clubs","diamonds","spades"]
deck = [card for card in itertools.product(suits,ranks)]


hands = [hand for hand in itertools.combinations(deck,5)]
