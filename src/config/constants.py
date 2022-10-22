"" " All project constants " ""

from src.config.types import CardSuitsType, CardValuesType

CARD_SUITS: list[CardSuitsType] = [
    "spades",
    "clubs",
    "hearts",
    "diamonds",
    "joker",
    "metacard",
]
CARD_VALUES: list[CardValuesType] = [
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

PLAYER_POSITIONS = ["top_center", "center_left", "center_right", "bottom_center"]


# Appearance config variables
CARD_BORDER_COLOR = "blue"
CARD_VALUE_COLOR = "blue"
