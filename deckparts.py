import random

class Suit():
	name =''
	image = ''

class Card():
	name = ''
	suit = Suit()
	value = ''
	abbr = ''
	lownum = 0
	highnum = 0

class Hand():
	_cards = []
	score = 0
	def AddCard(self, card):
		self._cards(card)

	def RemoveCard(self,index):
		self._cards.remove(index)

	def GetCardsInHand(self):
		return self._cards

class Player():
	name = ''
	hand = Hand()
	



class Deck():
	cards = []

	def __init__(self):
		self._build()

	def _build(self):
		for s in self._getsuits():
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

		     	self.cards.append(card)

	def _getsuits(self):
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
		return suits

	def Shuffle(self,times):
		shuffled_deck = []
		max_cards = len(self.cards)
		for i in range(0,max_cards):
			card_index = random.randint(0, max_cards-1)
			shuffle_card = self.cards[card_index]
			if shuffle_card in self.cards: 
					self.cards.remove(shuffle_card)
			if shuffle_card in shuffled_deck:
				raise Exception(str.format("ERROR -- The {} of {} is already in this deck!",shuffle_card.value,shuffle_card.suit.name))
			shuffled_deck.append(shuffle_card)
			max_cards-=1
		self.cards = shuffled_deck
		if times-1>0:
			self.Shuffle(times-1)