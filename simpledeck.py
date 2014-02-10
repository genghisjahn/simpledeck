from deckparts import Deck

deck=Deck()
deck.Shuffle(10)

for c in deck.cards:
     print(str.format("{} of {}",c.name,c.suit.name))
