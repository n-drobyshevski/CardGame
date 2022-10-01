""" All project constants """
import types

from src.config.types import CardTypesType, CardValuesType

CARD_TYPES: CardTypesType = ["spades", "clubs", "hearts", "diamonds", "joker", "meta"]
CARD_VALUES: CardValuesType = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "V",
    "C",
    "Q",
    "K",
]
METACARD_VALUES: list[str] = [str(x) for x in range(1, 22)]
CARD_QUANTITY: int = 78
CARD_ID: list[int] = [x for x in range(CARD_QUANTITY + 1)]
