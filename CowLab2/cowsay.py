from heifer_generator import HeiferGenerator
import sys
    

def list_cows(cows):
    for i in cows:
        print(i.name, end = " ")
    
def find_cow(name, cows):
    for i in cows:
        if i.name == name:
            return i
        
def main():
    #gets list of cows
    if sys.argv[1] == '-l':
        cow_list = HeiferGenerator.get_cows()
        print("Cows available: ", end='')
        list_cows(cow_list)
    #searches for the cow to display
    elif sys.argv[1] == '-n':
        current_cow = None
        cow_list = HeiferGenerator.get_cows()
        cow = sys.argv[2]
        current_cow = find_cow(cow, cow_list)
        if current_cow == None:
            print("Could not find " + sys.argv[2] + " cow!")
        else:
            message = ''
            message_list = sys.argv[3:len(sys.argv)]
            for i in message_list:
                message += i
                message += ' '
            print(message)
            print(current_cow.image)
            if current_cow.name == 'dragon' or current_cow.name == 'ice-dragon':
                if current_cow.can_breathe_fire() == True:
                    print("This dragon can breathe fire.")
                else:
                    print("This dragon cannot breathe fire.")
                    
    #default cow with message          
    else:
        cow_list = HeiferGenerator.get_cows()
        current_cow = find_cow('heifer', cow_list)
        message = ''
        message_list = sys.argv[1:len(sys.argv)]
        for i in message_list:
            message += i
            message += ' '
        print(message)
        print(current_cow.image)
        
    

           
if __name__ == '__main__':
    main()