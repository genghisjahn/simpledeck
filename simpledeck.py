from deckparts import Suit,Card,Deck

suit_h = Suit()
suit_h.name = 'Hearts'

suit_s = Suit()
suit_s.name = 'Spades'

suit_c = Suit()
suit_c.name = 'Clubs'

suit_d = Suit()
suit_d.name = 'Diamonds'

suits = []
suits.append(suit_h)
suits.append(suit_s)
suits.append(suit_c)
suits.append(suit_d)



deck=Deck()

for s in suits:
     for c in range(1, 14):
     	card = Card()
     	card.suit = s
     	card.highnum = c
     	card.lownum = c
     	if c==1:   		
     		card.name = 'Ace'
     		card.abbr = 'A'
     		card.highnum=14
     		card.lownum=1
     	elif c==11:
     		card.name = 'Jack'
     		card.abbr = 'J'
     	elif c==12:
     		card.name = 'Queen'
     		card.abbr = 'Q'
     	elif c==13:
     		card.name = 'King'
     		card.abbr = 'K'
     	else:
     		card.name = str(c)
     		card.abbr = str(c)

     	deck.cards.append(card)

deck.Shuffle(1)     		

for c in deck.cards:
	print(str.format('The card is the {} of {}',c.name, c.suit.name))


