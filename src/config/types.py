"""All game custom types"""
from typing import Literal

CardDataType = dict[int : dict[Literal["value"] : str, Literal["suit"] : str]]

PlayerDataType = dict[Literal["id"] : int, Literal["hand"] : list]
PlayerHandType = list[CardDataType]

CardSuitsType = Literal["spades", "clubs", "hearts", "diamonds", "metacard", "joker"]
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
