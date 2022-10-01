from random import randint


class Player:
    def __init__(self, init_hand) -> None:
        self.hand = init_hand
        self.id = self.create_id()

    def get_data(self):
        """Returns player data"""
        return {"id": self.id, "hand": self.hand}

    def take_card(self, deck):
        pass

    def put_card(self, card_id):
        """delete card from self.hand and returns it"""
        for i in len(self.hand):
            if self.hand[i].card_id == card_id:
                return self.hand.pop(i)
        return None

    def create_id(self):
        return randint(0, 9999)

    def __repr__(self) -> str:
        return f"Player: {self.id}"

    def __str__(self) -> str:
        return f"Player: {self.id}"
