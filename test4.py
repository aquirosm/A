from typing import List

class Country:
    """A class to represent a country."""

    # Class variable
    PLANET = "Earth"

    def __init__(self, name: str, capital: str, population: int, language: str, other_cities: List[str] = None):
        """
        Initialize a Country object.

        Args:
            name (str): The name of the country.
            capital (str): The capital city of the country.
            population (int): The population of the country.
            language (str): The primary language spoken in the country.
            other_cities (List[str], optional): A list of other major cities. Defaults to an empty list.
        """
        self.name = name
        self.capital = capital
        self.population = population
        self.language = language
        self.other_cities = other_cities if other_cities else None
    def add_population(self, births: int):
            self.population += births


CRI = Country("Costa Rica", "San Jose", 5000000, "Spanish")

print(CRI.name)
print(CRI.language)
print(CRI.other_cities)


CRI.other_cities = ["Heredia", "Cartago", "Alajuela"]

print(CRI.other_cities)

CRI.other_cities.append("Liberia")

print(CRI.other_cities)

print(CRI.population)

CRI.add_population(100)

print(CRI.population)