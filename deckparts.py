import itertools
import random


SUITS = set(['Hearts', 'Spades', 'Clubs', 'Diamonds'])

FACE_CARDS = {
    1: {
        'name': 'Ace',
                'abbr': 'A',
                'highnum': 14,
                'lownum': 1,
    },
    11: {
        'name': 'Jack',
                'abbr': 'J',
                'highnum': 11,
                'lownum': 11,
    },
    12: {
        'name': 'Queen',
                'abbr': 'Q',
                'highnum': 12,
                'lownum': 12,
    },
    13: {
        'name': 'King',
                'abbr': 'K',
                'highnum': 13,
                'lownum': 13,
    },
}


class Card(object):

    def __init__(self, suit, name, abbr, high_num, low_num):
        self.suit = suit
        self.name = name
        self.abbr = abbr
        self.high_num = high_num
        self.low_num = low_num

    def __unicode__(self):
        return "{s.name} of {s.suit}".format(s=self)

    def __str__(self):
        return self.__unicode__()


class Hand(object):

    def __init__(self):
        self.cards = set()
        self.score = 0

    def add_card(self, card):
        self.cards.add(card)

    def remove_card(self, card):
        self.cards.remove(card)


class Player(object):

    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class Deck(object):

    def __init__(self):
        self.cards = [self._create_card(s, c) for s, c in itertools.product(SUITS, range(1, 14))]

    def _create_card(self, suit, value):
        if value in FACE_CARDS:
            return Card(suit, FACE_CARDS[value]['name'], FACE_CARDS[value]['abbr'],
                        FACE_CARDS[value]['highnum'], FACE_CARDS[value]['lownum'])
        else:
            return Card(suit, str(value), str(value), value, value)

    def shuffle(self, numshuffles):
        for i in xrange(numshuffles):
            random.shuffle(self.cards)


class Game(object):

    def __init__(self, max_players=0, cards_per_hand=0):
        self.deck = Deck()
        self.players = set()
        self.max_players = max_players
        self.cards_per_hand = cards_per_hand

    def add_player(self, player):

        if len(self.players) <= self.max_players:
            self.players.add(player)
        else:
            raise Exception(
                str.format("Max players {} are already in the game.", self.max_players))

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)

    def deal(self):
        for i in range(0, self.cards_per_hand):
            for player in self.players:
                player.hand.add_card(self.deck.cards.pop())

    def scorehand(this, hand):
        if this._has_pair(hand):
            return "Has at least 1 pair!"
        else:
            return "No pairs found."

    def _has_pair(this, hand):
        result = []
        for card in hand.cards:
            pair_present = this._filterbyvalue(hand.cards, card)
            if len(list(pair_present)) == 2:
                result.append(card.high_num)

        return result

    def _is_straight(hand):
        # use this
        # http://stackoverflow.com/questions/2429073/check-if-the-integer-in-a-list-is-not-duplicated-and-sequential
        return False

    def _filterbyvalue(self, seq, value):
        for el in seq:
            if el.high_num == value.high_num:
                yield el
