class Country:
    planet = "Earth"

    def __init__(self, name, capital, population, language, other_cities):
        self.name = name
        self.capital = capital
        self.population = int(population)
        self.language = language
        self.other_cities = []

    def add_city(self, city):
        self.other_cities.append(city)

    def add_population(self, births):
        self.population = self.population + int(births)


USA = Country("United States", "Washington DC", 320000000, "English", "")
CRI = Country(name="Costa Rica", language = "Spanish", population = 5000000, capital = "San Jose", other_cities = "")


print(USA.name)
print(USA.capital)
print(USA.population)
print(USA.planet)
print(USA.other_cities)

print("*****Next country*****")


print(CRI.name)
print(CRI.capital)
print(CRI.population)
print(CRI.planet)
print(CRI.other_cities)

USA.add_city("Chicago")
CRI.add_city("Heredia")
USA.add_city("Los Angeles")
USA.add_city("Ohio")
USA.add_city("Phoenix")
USA.add_city("Atlanta")
CRI.add_city("Heredia")
CRI.add_city("Alajuela")



print("*****After adding cities*****")
print(USA.other_cities)
print(CRI.other_cities)