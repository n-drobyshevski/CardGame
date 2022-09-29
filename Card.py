class Card():
    # Ajoute ID 
    def __init__(self, value:str, type:str) -> None:
        self.type = type
        self.value = value
    
    # def get_card(self):
    def __repr__(self) -> str:
      return f"value: {self.value}, type:{self.type}"
    
    def __str__(self) -> str:
      return f"value: {self.value}, type:{self.type}"
  
    def get_data(self):
        return {"value": {self.value}, "type":{self.type}}
    
class  MetaCard(Card):
    def __init__(self,value:str) -> None:
        super().__init__(value=value, type="meta")