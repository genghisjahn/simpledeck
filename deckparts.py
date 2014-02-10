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

class Hand():
	cards = []
	score = 0

class Player():
	name = ''
	_hand = Hand()
	def AddCard(self, card):
		self._hand.cards(card)

	def RemoveCard(self,index):
		self._hand.cards.remove(index)

	def GetCardsInHand(self):
		return self._hand.cards



class Deck():
	cards = []
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