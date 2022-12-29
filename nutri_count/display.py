from dataclasses import dataclass  # https://realpython.com/python-data-classes/
from typing import List
from eintrag import Eintrag

#Datatypes für Addition
@dataclass
class Display:
    eintraege: List[Eintrag]
    total_energy: float = 0.0
    total_fat: float = 0.0
    total_fat_acids: float = 0.0
    total_carbs: float = 0.0
    total_sugar: float = 0.0
    total_protein: float = 0.0
    total_salt: float = 0.0
