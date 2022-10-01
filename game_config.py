""" All project constants """

from typing import Literal

CARD_TYPES = ["Spades", "Clubs", "Hearts", "Diamonds", "JOKER", "META"]
CARD_VALUES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "C", "Q", "K"]
METACARD_VALUES = [str(x) for x in range(1, 22)]
CARD_QUANTITY = 78
CARD_ID = [x for x in range(CARD_QUANTITY + 1)]


CardTypesType = Literal["Spades", "Clubs", "Hearts", "Diamonds"]
CardValuesType = Literal[
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
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "V",
    "C",
    "Q",
    "K",
    "JOKER",
]
