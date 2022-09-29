from random import randint
from Player import Player
from Card import Card, MetaCard

CARD_TYPES = ["Spades", "Clubs", "Hearts", "Diamonds"]
CARD_VALUES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "C", "Q", "K"]
METACARD_VALUES = [str(x) for x in range(1, 22)]


class Game:
    def __init__(self) -> None:
        self.players_count = 4
        self.deck = self.create_deck()
        self.players = self.create_players()

    def create_deck(self):
        deck = []
        for tp in CARD_TYPES:
            for vl in CARD_VALUES:
                card = Card(value=vl, type=tp)
                deck.append(card.get_data())

        for vl in METACARD_VALUES:
            card = MetaCard(value=vl)
            deck.append(card.get_data())

        joker = MetaCard(value="JOKER")
        deck.append(joker.get_data())
        return deck

    def get_random_card(self):
        card_index = randint(0, len(self.deck) - 1)
        card = self.deck[card_index]
        self.deck.pop(card_index)
        return card

    def create_player_hand(self):
        hand = [self.get_random_card() for _ in range(18)]
        return hand

    def compare_cards(self):
        pass

    def create_players(self):
        return [Player(self.create_player_hand()) for _ in range(4)]
