from pakuri import Pakuri
from pakudex import Pakudex


def menu():
    #Menu Function
    print('Pakudex Main Menu')
    print('-----------------')
    print('1. List Pakuri')
    print('2. Show Pakuri')
    print('3. Add Pakuri')
    print('4. Evolve Pakuri')
    print('5. Sort Pakuri')
    print('6. Exit')
    print(" ")

def main():
    #Main Function
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        #Try catch statment does not allow for string or negative numbers to be entered
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
        except ValueError:
            print("Please enter a valid size.")
            continue
        if capacity < 0:
            print("Please enter a valid size.")
            continue
        else:
            break
    print("The Pakudex can hold " + str(capacity) + " species of Pakuri.")
    current_pakudex = Pakudex(capacity)
    active = True
    #Program loop
    while active:
        menu()
        #Try catch does not allow for strings to be entered
        try:
            choice = int(input("What would you like to do? "))
        except ValueError:
            print("Unrecognized menu selection!")
            continue
        #Lists the pakuri in the pakudex if the pakudex has entries in it
        if choice == 1:
            paku_list = current_pakudex.get_species_array()
            if paku_list == None:
                print("No Pakuri in Pakudex yet!")
                continue
            else:
                print("Pakuri In Pakudex: ")
                for i in range(0,len(paku_list)):
                    num = str(i + 1)
                    print(num + ". " + paku_list[i])
            print(" ")
        #Displays the stats of a species in the pakudex
        elif choice == 2:
            species = input("Enter the name of the species to display: ")
            stat_list = current_pakudex.get_stats(species)
            if stat_list == None:
                continue
            else:
                print("Species: " + species)
                print("Attack: " + str(stat_list[0]))
                print("Defense: " + str(stat_list[1]))
                print("Speed: " + str(stat_list[2]))
        #Gets the size of the pakudex and if it is not equal to the capacity it allows for pakuri to be added
        elif choice == 3:
            size = current_pakudex.get_size()
            if size == capacity:
                print("Error: Pakudex is full!")
            else:
                species = input("Enter the name of the species to add: ")
                current_pakudex.add_pakuri(species)
        #Evolves a pakuri
        elif choice == 4:
            species = input("Enter the name of the species to evolve: ")
            current_pakudex.evolve_species(species)
        #Sorts the pakuri by name in the pakudex
        elif choice == 5:
            current_pakudex.sort_pakuri()
        #Exits program loop
        elif choice == 6:
            print("Thanks for using Pakudex! Bye!")
            active = False
        else:
            print("Unrecognized menu selection!")
            
    
if __name__ == "__main__":
    main()