from random import randint 
class Player():
    def __init__(self, init_hand) -> None:
        self.hand = init_hand
        self.id = self.create_id()
        
    def get_data(self):
        return {"id": self.id,"hand":self.hand }
        
    def take_card(self, deck):
        pass
    
    def put_card(self, card):
        pass
        
    def create_id(self):
        return randint(0,9999)
    
    def __repr__(self) -> str:
        return f"Player: {self.id}"
        
    def __str__(self) -> str:
        return f"Player: {self.id}"