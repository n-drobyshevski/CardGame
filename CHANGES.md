# Changes

--- 887280

    - Change: Card(), 'type' argument -> 'card_type'

    - Change: Card(), new argument 'id', new card representation ```{ id: {value:str, type:str }}```
      - !!! Change overwritten after commit 887280 !!!

    - Change: Player(), put_card() implementation

--- 3e133a

    - Create: config/constants.py with all game constants
    - Create: config/types.py with all game custom types
    - Add: type checking for all functions

    - Breaking change: all python scripts were moved to src/ directory

    - Change: card types to lowercase ("Diamonds"->"diamonds")
    - Add: type checking to constants in config/constants.py

--- 1508b8

    - Rename: card_type to cart_suit

---97b572

    - Change: CardData representation to {'id':id, 'value':value, 'suit':suit}
