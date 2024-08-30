from Entity import Entiti
from dataclasses import dataclass
import Car

@dataclass
class Client(Entiti):
    id:int
    name: str
    number:str
    cars:list(Car)

    def __init__(self, id:int, number:str, first_name:str, family_name:str, last_name:str):
        self.id = id
        self.number = number
        self.name = first_name+family_name+last_name

    def set_car(car:Car)->cars:
        cars.append(car)