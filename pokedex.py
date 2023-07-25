class Pokemon:
    def __init__(self,entry,name,type,description):
        self.entry = entry
        self.name = name
        self.type = type
        self.description = description
        self.is_caught = False

    def speak(self):
        print('"' + self.name + '! ' + self.name + '!"')

    def catch(self):
        self.is_caught=True
        print("You caught " + self.name + "!")

    def pokedex(self):
        print("--------------------------------------")
        print("#" + str(self.entry) + " " + self.name)
        if len(self.type)==1:
            print(str(self.type[0]) + " type Pokemon")
        if len(self.type)==2:
            print(str(self.type[0]) + " and " + str(self.type[1]) + " type Pokemon")
        print("Description: " + self.description)
        if self.is_caught == True:
            print("You have caught this Pokemon.")
        if self.is_caught == False:
            print("You have not caught this Pokemon.")
        print("--------------------------------------")

pikachu = Pokemon(25,"Pikachu",["Electric"],"It keeps its tail raised to monitor its surroundings. If you yank its tail, it will try to bite you.")

chinchou = Pokemon(170,"Chinchou",["Water","Electric"],"It shoots positive and negative electricity between the tips of its two antennae and zaps its enemies.")

genesect = Pokemon(649,"Genesect",["Bug","Steel"],"This Pokémon existed 300 million years ago. Team Plasma altered it and attached a cannon to its back.")

pikachu.pokedex()
chinchou.pokedex()
genesect.pokedex()

pikachu.catch()
pikachu.speak()

genesect.catch()

pikachu.pokedex()
chinchou.pokedex()
genesect.pokedex()


