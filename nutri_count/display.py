from dataclasses import dataclass  # https://realpython.com/python-data-classes/
from typing import List

#datatypes für einzelnen Eintrag
@dataclass
class Eintrag:
    product_name: str
    amount: float
    energy: float
    fat: float
    fat_acids: float
    carbs: float
    sugar: float
    protein: float
    salt: float

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

@dataclass
class Compare:
    energy: float = 0.0
    fat: float = 0.0
    fat_acids: float = 0.0
    carbs: float = 0.0
    sugar: float = 0.0
    protein: float = 0.0
    salt: float = 0.0
    is_energy_good: bool = False