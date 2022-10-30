"""All game custom types"""
# from ..Card import Card
from typing import Literal, TypeAlias, Any

CardSuitsType: TypeAlias = Literal[
    "spades", "clubs", "hearts", "diamonds", "metacard", "joker"
]

# str here cause of metacard values
CardValuesType: TypeAlias = (
    str
    | Literal[
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
)

PlayerRoles: TypeAlias = Literal["petit", "garde", "garde sans", "garde contre", ""]
