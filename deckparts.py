import itertools
import random
import operator


SUITS = set(['Hearts', 'Spades', 'Clubs', 'Diamonds'])
HAND_RESULTS = [(
    'High Card', 10), ('Pair', 20), ('Two Pair', 30), ('Three of a Kind', 40), ('Straight', 50),
    ('Flush', 60), ('Full House', 70), ('Four of a Kind', 80), ('Straight Flush', 90), ('Royal Flush', 100)]

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

    def scorehand(self):
        combos = list(itertools.combinations(self.cards, 5))
        highest = 0
        highest_hand = combos[0]
        for combo in combos:
            current = self.scorehand_5(combo)

            if current > highest:
                highest = current
                highest_hand = combo

            if current == highest:
                highest_hand = self._compare_same(highest_hand, combo, highest, current)

        return (highest, highest_hand)

    def _compare_same(self, hand1, hand2, score1, score2):
        result = hand1
        if score1[1] == 10:
            result = self._dif_high_card(list(hand1), list(hand2))
        if score1[1] == 20:
            result = self._dif_high_card(list(hand1), list(hand2))
        """
        10 is highscard
        20 is pair
        30 is two pair
        40 is three of kind
        50 is straight
        60 is flush
        70 is full House
        80 is four of kind
        90 is straight flush
        100 is Royal flush
        """
        return result

    def _dif_high_card(self, hand1, hand2):
        result = hand1
        hand1.sort(key=operator.attrgetter("high_num"), reverse=True)
        hand2.sort(key=operator.attrgetter("high_num"), reverse=True)
        for card_hand1, card_hand2 in zip(hand1, hand2):
            if card_hand1.high_num > card_hand2.high_num:
                result = hand1
                break
            elif card_hand1.high_num < card_hand2.high_num:
                result = hand2
                break
        else:
            pass
            # return "It's a tie!"  # this should throw an excpetion

        return result

    def _dif_two_pair(self, hand1, hand2):
        result = hand1
        # get pairs from each hand.
        # compare the highest pair from each hand, highest wins.
        # if they are same rank, compare the lesser pair from each hand, highest wins.
        # if they are the same, compare remaining kicker card, higher kicker wins.
        # if top pair, bottom pair and kicker are equal, throw tie excetion.
        return result

    def _dif_three_kind(self, hand1, hand2):
        result = hand1
        # same as _dif_pair only pull the three matching value cards and if tie,
        # compare the two remaining kickers.
        return result

    def _dif_flush(self, hand1, hand2):
        # If both hands are flushes, then just get the
        # flush with the highest card(s).
        return self._dif_high_card(hand1, hand2)

    def _print_5_card_hand(self, hand):
        print ('-' * 10)
        for card in hand:
            print "%s%s" % (' ' * 8, card)

    def scorehand_5(self, card5):
        result = HAND_RESULTS[0]

        pairs = self._of_a_kind(card5, 2, "Pair of")[0]
        threes = self._of_a_kind(card5, 3, "Three of a kind, three ")[0]
        fours = self._of_a_kind(card5, 4, "Four of a kind, four ")[0]
        straight = self._has_straight(card5)[0]
        flush = self._has_flush(card5)[0]
        if len(pairs) == 2:
            result = HAND_RESULTS[2]
        elif pairs and not threes == 1:
            result = HAND_RESULTS[1]

        if not pairs and threes:
            result = HAND_RESULTS[3]

        if fours:
            result = HAND_RESULTS[7]

        # No need to check this if there
        # is another scored hand

        if straight:
            result = HAND_RESULTS[4]

        if flush:
            result = HAND_RESULTS[5]

        if pairs and threes:
            result = HAND_RESULTS[6]

        if straight and flush:
            result = HAND_RESULTS[8]

        return result

    def _of_a_kind(self, card5, value, score_message):
        result = []
        card_val = 0
        for card in card5:
            kind_present = self._filterbyvalue(self.cards, card)
            if len(list(kind_present)) == value:
                card_val = card.high_num
                new_val = str.format("{} {}s.", score_message, card.name)
                if not new_val in result:
                    result.append(new_val)
        return ((result, card_val))

    def _has_flush(self, card5):
        result = []
        for card in card5:
            flush_present = self._filterbysuit(self.cards, card)
            if len(list(flush_present)) == 5:
                new_val = str.format("Flush {}", card.suit)
                if not new_val in result:
                    result.append(new_val)
                    break
        return ((result, 0))

    def _filterbyvalue(self, seq, value):
        for el in seq:
            if el.high_num == value.high_num:
                yield el

    def _filterbysuit(self, seq, value):
        for el in seq:
            if el.suit == value.suit:
                yield el

    def _has_straight(self, card5):
        result = []
        low_nums = []
        high_nums = []
        for card in card5:
            low_nums.append(card.low_num)
            high_nums.append(card.high_num)

        if self._sequential_ints(low_nums) or self._sequential_ints(high_nums):
            result.append("Straight.")

        return ((result, 0))

    def _sequential_ints(self, item_vals):
        return len(item_vals) == len(set(item_vals)) == max(item_vals) - min(item_vals) + 1


class Player(object):

    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class ScoreData(object):

    def __init__(self, score, high_card1, high_card2=0):
        self.score = score
        self.high_card1 = high_card1
        self.high_card2 = high_card2

    def __unicode__(self):
        return unicode(self.score)

    def __str__(self):
        return str(self.score)


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
