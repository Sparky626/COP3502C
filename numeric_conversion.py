

def menu():
    # Function prints decoding menu
    print("Decoding Menu")
    print("-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit")


def hex_string_decode(hex):
    # Function decodes an entire hexadecimal string
    hexadecimalTotal = 0
    for i in range(len(hex)):
        if hex[i] == "0" or hex[i] == "x":
            currentIgnore = hex[i]
        elif hex[i].isalpha() == True:
            currentNum = hex_char_decode(hex[i])
            hexadecimalTotal = hexadecimalTotal + (currentNum * 16 ** (len(hex) - i - 1))
        else:
            currentNum = int(hex[i])
            hexadecimalTotal = hexadecimalTotal + (currentNum * 16 ** (len(hex) - i - 1))
    return hexadecimalTotal

def hex_char_decode(digit):
    # Function returns a number depending on what letter is in the parameter
    currentNum = 0
    if digit == "A" or digit == "a":
        currentNum = 10
    elif digit == "B" or digit == "b":
        currentNum = 11
    elif digit == "C" or digit == "c":
        currentNum = 12
    elif digit == "D" or digit == "d":
        currentNum = 13
    elif digit == "E" or digit == "e":
        currentNum = 14
    elif digit == "F" or digit == "f":
        currentNum = 15
    return currentNum


def binary_string_decode(binary):
    # Function decodes a binary string
    binaryTotal = 0
    for i in range(len(binary)):
        if str(binary[i]) == "1":
            binaryTotal = binaryTotal + 2**(len(binary)-i-1)
    return binaryTotal


def binary_to_hex(binary):
    # Function decodes binary and then converts to hexadecimal
    toHex = binary_string_decode(binary)
    currentTotal = toHex
    hexString = ""
    #Reverse decimal to hex while loop
    while currentTotal % 16 != 0:
        remainder = currentTotal % 16
        currentTotal = int(currentTotal/16)
        if remainder < 10:
            hexString += str(remainder)
        elif remainder == 10:
            hexString += 'A'  
        elif remainder == 11:
            hexString += 'B'   
        elif remainder == 12:
            hexString += 'C'   
        elif remainder == 13:
            hexString += 'D'    
        elif remainder == 14:
            hexString += 'E'  
        elif remainder == 15:
            hexString += 'F' 
    hexString = hexString [::-1] 
    return hexString


def main():
    #Main program loop, keeps entire program going
    program_active = True
    menu()
    while program_active:
        print(" ")
        menu_choice = int(input("Please enter an option: "))
        if menu_choice == 1:
            #calls hexstringdecode
            num_string = input("Please enter the numeric string to convert: ")
            result = hex_string_decode(num_string)
            print("Result: " + str(result))
            print(" ")
            menu()
        elif menu_choice == 2:
            #calls binarystringdecode
            num_string = input("Please enter the numeric string to convert: ")
            result = binary_string_decode(num_string)
            print("Result: " + str(result))
            print(" ")
            menu()
        elif menu_choice == 3:
            #calls binartytohex
            num_string = input("Please enter the numeric string to convert: ")
            result = binary_to_hex(num_string)
            print("Result: " + str(result))
            print(" ")
            menu()
        elif menu_choice == 4:
            #ends program
            program_active = False
            print("Goodbye!")
        else:
            print("")

if __name__ == "__main__":
    main()
