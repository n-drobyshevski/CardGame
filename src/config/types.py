"""All game custom types"""
# from ..Card import Card
from typing import Annotated, Literal, Type, TypeAlias, TypedDict, Any, TypeGuard

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
# CardDataType:TypeAlias = dict[Literal["id","value", "suit",], str | int]
class CardDataType(TypedDict):
    id: int
    value: CardValuesType
    suit: CardSuitsType


# -- PLAYER TYPES
# def is_card_list(val: list[Card]) -> TypeGuard[list[Card]]:


# PlayerDataType:TypeAlias = dict[Literal["id","hand"], int| list]
class PlayerDataType(TypedDict):
    id: int
    hand: list
