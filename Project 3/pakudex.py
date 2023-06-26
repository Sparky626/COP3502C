from pakuri import Pakuri

class Pakudex:
    #Pakudex constructor
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.Pakudex = []
    #Gets current size of Pakudex
    def get_size(self):
        return len(self.Pakudex)
    #Gets max capacity of Pakudex
    def get_capacity(self):
        return self.capacity
    #Gets a list of all of the species entered into the pakudex
    def get_species_array(self):
        if len(self.Pakudex) == 0:
           return None
        else:
            species_array = []
            for obj in self.Pakudex:
                species_array.append(obj.species)
            if len(species_array) == 0:
                return False
            else:
                return species_array
    #Gets stats of a species in the pakudex
    def get_stats(self, species):
        if len(self.Pakudex) == 0:
            print("Error: No such Pakuri!")
            return None
        else:
            for obj in self.Pakudex:
                if obj.species == species:
                    stats = []
                    stats.append(obj.attack)
                    stats.append(obj.defense)
                    stats.append(obj.speed)
                    return stats
                else:
                    print("Error: No such Pakuri!")
                    return None
    #Sort the pakuri in the pakudex alphabetically
    def sort_pakuri(self):
        self.Pakudex.sort(key=lambda x: x.species)
        print("Pakuri have been sorted!")
    #Add pakuri to a pakudex 
    def add_pakuri(self, species):
        if len(self.Pakudex) == 0:
            self.Pakudex.append(Pakuri(species))
            print("Pakuri species " + species + " successfully added!")
            return True
        else:
            for obj in self.Pakudex:
                if obj.species == species: 
                    print("Error: Pakudex already contains this species!")
                    return False
                else:           
                    self.Pakudex.append(Pakuri(species))
                    print("Pakuri species " + species + " successfully added!")
                    return True
    #Evolve a pakuri in the pakudex
    def evolve_species(self, species):
        evolved = False
        for obj in self.Pakudex:
            if obj.species == species:
                obj.evolve()
                evolved = True
                print(species + "has evolved!")             
                return True
            else:
                continue
        if evolved == False:
            print("Error: No such Pakuri!")
            return False
        
        