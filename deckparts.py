import random

class Suit():
	name =''
	image = ''

class Card():
	suit = Suit()
	value = ''
	abbr = ''
	lownum = 0
	highnum = 0

class Deck():
	cards = []
	def Shuffle(self,times):
		shuffled_deck = []
		card_index = random.randint(0, 51)
		shuffle_card = self.cards[card_index]
		if shuffle_card in self.cards: 
				self.cards.remove(shuffle_card)
		shuffled_deck.append(shuffle_card)
		self.cards = shuffled_deck