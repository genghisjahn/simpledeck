from deckparts import Game, Player


def main():

    while True:
        game = Game(max_players=4, cards_per_hand=5)

        p1 = Player("Adam")
        p2 = Player("Brad")
        p3 = Player("Jerom")
        p4 = Player("Malik")

        game.add_player(p1)
        # game.add_player(p2)
        # game.add_player(p3)
        # game.add_player(p4)

        game.deck.shuffle(10)
        game.deal()
        found_flag = False
        for player in game.players:

            print player
            for card in player.hand.cards:
                print "%s%s" % (' ' * 8, card)

            for p in player.hand.scorehand():
                print str.format("score: {}", p)
                if p.startswith('Straight'):
                    found_flag = True
                    break

            if found_flag == True:
                break
            print "-" * 10
        if found_flag == True:
            break


def print_deck(deck):
    for card in deck.cards:
        print "%s%s" % (' ' * 8, card)

if __name__ == '__main__':
    main()
