from deckparts import Game, Player

def main():
	game = Game(max_players=4, cards_per_hand=5)

	p1 = Player("Adam")
	p2 = Player("Brad")
	p3 = Player("Jerom")
	p4 = Player("Malik")

	game.add_player(p1)
	game.add_player(p2)
	game.add_player(p3)
	game.add_player(p4)

	#game.deck.shuffle(0)
	#game.deal()
	"""
	print game.players
	for player in game.players:
		print player
		for card in player.hand.cards:
			print "%s%s" % (' '*8, card)
	"""
	for card in game.deck.cards:
		print "%s%s" % (' '*8, card)

if __name__ == '__main__':
	main()

