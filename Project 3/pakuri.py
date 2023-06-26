class Pakuri:
    
    #Constructor for Pakuri
    def __init__(self, species):
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13
    #Returns pakuri species
    def get_species(self):
        return self.species
    #Returns pakuri attack stat
    def get_attack(self):
        return self.attack
    #Returns pakuri defense stat
    def get_defense(self):
        return self.defense
    #Returns pakuri speed stat
    def get_speed(self):
        return self.speed
    #Sets new attack for the pakuri
    def set_attack(self, new_attack):
        self.attack = new_attack
    #Evolves pakuri and increases the stats
    def evolve(self):
        self.attack = self.attack*2
        self.defense = self.defense*4
        self.speed = self.speed * 3

        
        
        