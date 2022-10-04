from .config.types import CardDataType
from .config.constants import CARD_ID, CARD_SUITS, CARD_VALUES, METACARD_VALUES


from .Card import Card, MetaCard


class Deck:
    def __init__(self):
        self.deck = self.create_deck()
        self.length = len(self.deck)

    def create_deck(self) -> list:
        current_card_id = 0
        deck = []

        # Adding common cards
        for tp in CARD_SUITS[:4]:
            for vl in CARD_VALUES:
                card = Card(value=vl, card_suit=tp, card_id=CARD_ID[current_card_id])
                current_card_id += 1
                deck.append(card.get_data())

        # Adding metacards
        for vl in METACARD_VALUES:
            card = MetaCard(value=vl, card_id=CARD_ID[current_card_id])
            current_card_id += 1
            deck.append(card.get_data())

        # Adding joker
        joker = Card(value="J", card_suit="joker", card_id=CARD_ID[current_card_id])
        deck.append(joker.get_data())
        return deck

    def get_card_by_id(self, id) -> CardDataType:
        for card in self.deck:
            if card["id"] == id:
                return card

    def __repr__(self) -> str:
        return f"{self.deck}"

    def __str__(self) -> str:
        return f"{self.deck}"
