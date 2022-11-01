from random import randint
from shutil import register_unpack_format
from typing import Optional, Tuple

from .Player import Player
from .Card import Card
from .Deck import Deck

from .config.types import CardSuitsType
from .config.constants import (
    PLAYER_POSITIONS,
)


class Game:
    # tip: Optional[TYPE] - means that arg can be TYPE or None
    def __init__(self, player_names: Optional[list[str]] = None) -> None:
        self.players_count = 4
        self.deck: list = Deck().deck
        self.players: list[Player] = self._create_players(player_names)
        self.round: int = 0
        # tip: data type is equals to [ (Card, Player), (..., ...), ...]
        self.table: list[
            Tuple[Card, Player]
        ] = []  # card and player that placed this card
        self.first_playing_player: Player = self.players[0]
        self.current_player: Player = self.first_playing_player

    # ------------- CARDS METHODS -----------------------------
    def get_random_card(self) -> Card:
        card_index = randint(0, len(self.deck) - 1)
        card = self.deck.pop(card_index)
        return card

    # tip: data arg type is equal to [ (Card, Player), (Card, Player), ...]
    def compare_cards(self, data: list[Tuple[Card, Player]], main_suit: CardSuitsType):
        highest_card = None
        wining_player = None
        for tpl in data:
            card = tpl[0]
            player = tpl[1]
            if card.suit == main_suit:
                if highest_card == None:
                    highest_card = card
                    wining_player = player
                elif highest_card.value < card.value:
                    highest_card = card
                    wining_player = player
        return highest_card, wining_player

    def get_card_by_id(self, id: int) -> Card:
        for card in self.deck:
            if card.id == id:
                return card
        raise Exception("requested id doesn't correspond to any card")

    # ------------ PLAYER RELATED METHODS --------------------
    def get_player_by_id(self, id: int):
        for player in self.players:
            if player.id == id:
                return player
        raise Exception("requested id doesn't correspond to any player")

    def get_next_player(self) -> Player:
        for index in range(len(self.players)):
            if self.players[index] == self.current_player:

                if self.players[index] == self.players[-1]:
                    # if current player is the last element of self.players return self.players[0]
                    res_player = self.players[0]
                else:
                    res_player = self.players[index + 1]

                self.current_player = res_player
                return res_player
        raise Exception("exception in get_next_player")

    # ---- PRIVATE METHODS (SHOULD NOT BE USED OUT OF CLASS)
    def _create_player_hand(self) -> list[Card]:
        return [self.get_random_card() for _ in range(18)]

    def _create_players(self, names) -> list[Player]:
        return [Player(self._create_player_hand(), name=names[i]) for i in range(4)]
