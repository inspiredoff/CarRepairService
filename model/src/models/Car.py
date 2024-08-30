from Entity import Entiti
from dataclasses import dataclass

@dataclass
class Car(Entiti):
    id:int
    name: str
    number:str

    def __init__(self, id:int, number:str, first_name:str, family_name:str, last_name:str):
        self.id = id
        self.number = number
        self.name = first_name+family_name+last_name
