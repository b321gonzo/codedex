class City:
    def __init__(self,name,country,state,population):
        self.name = name
        self.country = country
        self.state = state
        self.population = population

nyc = City("New York City","USA","New York",7888000)
conwayar = City("Conway","USA","Arkansas",65000)


print(vars(nyc))
print(vars(conwayar))
