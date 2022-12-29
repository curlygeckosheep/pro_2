from dataclasses import dataclass  # https://realpython.com/python-data-classes/

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
