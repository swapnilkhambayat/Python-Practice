#Following program shows the use of list operator and helper functions
"""Step 1 - Create a list for a standard deck of cards
   Step 2 - Randomly choose five cards to add to a player's hand
   Expected Output:
    There are 52 cards in the deck.
    Dealing ...
    There are 47 cards in the deck.
    Player has the following cards in their hand:
    ['Jack of Hearts', 'Queen of Hearts', '4 of Spades', 'Ace of Hearts', '9 of Diamonds']"""

import random as r

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
pack = []
select_hand = []

#total_cnt = len(suits) * len(ranks)

#print(f'There are {total_cnt} cards in the deck.')

for  suit in suits:
    for rank in ranks:
        pack.append(f'{rank} of {suit}') 

print(f'There are {len(pack)} cards in the deck.')
print('Dealing...')

select_hand = r.choices(pack, k=5)

for i in select_hand:
    pack.remove(i)

print(f'There are {len(pack)} cards in the deck.' )
print('Player has the following cards in their hand:')
print(select_hand)

