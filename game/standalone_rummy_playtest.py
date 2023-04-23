import random
from enum import Enum

class Suits(Enum):
    clubs = 0
    diamonds = 1
    hearts = 2
    spades = 3

class Players(Enum):
    player = 0
    natsuki = 1

__CARD_SUITS = [
    Suits.clubs,
    Suits.diamonds,
    Suits.hearts,
    Suits.spades
]


class CardBundle(object):
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards



    def __len__(self):
        return len(self.cards)

    @property
    def top_card(self):
        return self.cards[-1]

    @property
    def last_card(self):
        return self.cards[0]

    def shuffle(self):
        random.shuffle(self.cards)

    def add_card(self, card):
        """Adds a card to the <top> of the bundle"""
        self.cards.append(card)

    def add_cards(self, cards):
        self.cards += cards

    def get_card_by_index(self, index):
        return self.cards[index]

    def remove_card(self, card):
        """
        Removes a card from bundle.
        If the card is known to be at the top or the bottom
        of the bundle it is highly recommended to instead use
        ´remove_top_card´ or ´remove_last_card´ respectively
        """
        self.cards.remove(card)

    def remove_top_card(self):
        return self.cards.pop(0)

    def remove_last_card(self):
        return self.cards.pop(-1)

    def remove_cards(self, cards):
        for card in cards:
            self.cards.remove(card)

    def contains_card(self, card):
        return card in self.cards

    def give_card(self, card, other_bundle):
        """
        Convenience wrapper functino

        Moves a card from this instance to another
        """
        CardBundle.move_card(self, card, other_bundle)

    @staticmethod
    def move_card(bundle1, card, bundle2):
        if not bundle1.contains_card(card):
            #TODO: log this instead
            raise Exception("tried to move a card out of a bundle which does not contain it")

        bundle1.remove_card(card)
        bundle2.add_card(card)

    @staticmethod
    def switch_cards(bundle1, bundle2, card1, card2):
        CardBundle.move_card(bundle1, card1, bundle2)
        CardBundle.move_card(bundle2, card2, bundle1)


class TableCardBundle(CardBundle):
    def __init__(self, cards, share_suit):
        if len(cards) < 3:
            #TODO: log this instead
            raise Exception("Table card bundles must contain at least 3 cards")
        self.share_suit = share_suit # true => cards share a suit; false=> cards share value
        super().__init__(cards)

    def can_add_card(self, card):
        check_suit_or_value = 0 if self.share_suit else 1
        return all(self.cards, lambda x: x[check_suit_or_value] == card[check_suit_or_value])

    def add_card(self, card):
        if not self.can_add_card(card):
            raise Exception("Cannot lay that card on the table")
        return super().add_card(card)


class CardsManager(object):
    def __init__(self):
        self.player_hand = CardBundle()
        self.natsuki_hand = CardBundle()
        self.deck = CardBundle()
        self.table = []

    def prepare_game(self, dealer):
        # More ewww
        self.now_playing = Players.natsuki if dealer == Players.player else Players.player

        if dealer == Players.player:
            __player_is_starting = 1

        else: #if dealer == Players.natsuki
            __player_is_starting = 0

        self.deck.add_cards(CardsManager.get_all_cards())
        self.deck.shuffle()

        for i in range(25):
            __card = random.choice(self.deck)
            if i % 2 == __player_is_starting:
                self.deck.give_card(__card, self.player_hand)
            else:
                self.deck.give_card(__card, self.natsuki_hand)

        #DEBUG:
        assert len(self.player_hand.cards) == 12+__player_is_starting
        assert len(self.natsuki_hand.cards) == 13-__player_is_starting



    @staticmethod
    def get_all_cards():
        """
        Is technically a little expensive
        so store and then use!

        <2, 10>  - regular value cards
        <11, 14> - jack, queen, king, ace
        15       - joker
        """

        #NOTE: Uglyyy pls remember to change this!!
        return [(suit, value) for suit in __CARD_SUITS for value in range(2, 15)]

    def get_current_player_cards(self):
        if self.now_playing == Players.player:
            return self.player_hand
        else:
            return self.natsuki_hand

class TurnEvent(object):
    def __init__(self):
        pass
