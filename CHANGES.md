# Changes

    - Change: Card(), 'type' argument -> 'card_type'
    - Change: Card(), new argument 'id', new card representation ```{ id: {value:str, type:str }}```
    - Change: Player(), put_card() implementation

---

    - Create: config/constants.py with all game constants
    - Create: config/types.py with all game custom types
    - Add: type checking for all functions

    - Breaking change: all python scripts were moved to src/ directory

    - Change: card types to lowercase ("Diamonds"->"diamonds")
    - Add: type checking to constants in config/constants.py
