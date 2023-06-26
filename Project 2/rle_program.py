from console_gfx import ConsoleGfx

def menu():
    print("RLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")
    print(" ")


def main():
    print("Welcome to the RLE image encoder!")
    print(" ")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    print(" ")
    print(" ")
    loaded_file = None
    active = True
    while active == True:
        menu()
        choice = int(input("Select a Menu Option: "))
        if choice == 1:
            file = input("Enter name of file to load: ")
            loaded_file = ConsoleGfx.load_file(file)
            print(" ")
        elif choice == 2:
            loaded_file = ConsoleGfx.test_image
            print("Test image data loaded.")
        elif choice == 3:
            rle_string = input("Enter an RLE string to be decoded: ")
            loaded_file = decode_rle(string_to_rle(rle_string))
        elif choice == 4:
            hex_string = input("Enter the hex string holding RLE data: ")
            loaded_file = decode_rle(string_to_data(hex_string))
        elif choice == 5:
            hex_string = input("Enter the hex string holding flat data: ")
            loaded_file = encode_rle(list(string_to_data(hex_string)))
        elif choice == 6:
            print("Displaying image...")
            if loaded_file == None:
                print("(no data)")
            else:
                ConsoleGfx.display_image(loaded_file)
            print(" ")
        elif choice == 7:
            if loaded_file == None:
                rle_string = "(no data)"
            else:
                rle_string = to_rle_string(encode_rle(loaded_file))
            print("RLE representation: " + rle_string)
        elif choice == 8:
            if loaded_file == None:
                rle_string = "(no data)"
            else:
                rle_string = to_hex_string(encode_rle(loaded_file))
            print("RLE hex values: " + rle_string)
        elif choice == 9:
            if loaded_file == None:
                flat_hex = "(no data)"
            else:
                flat_hex = to_hex_string(loaded_file)
            print("Flat hex values: " + flat_hex)
        elif choice == 0:
            active = False
        else:
            print("Error! Invalid Output")


#Translates data to a hex string
def to_hex_string(data):
    hex_string = ""
    for i in range(len(data)):
        if data[i] == 10:
            hex_string += 'a'
        elif data[i] == 11:
            hex_string += 'b'
        elif data[i] == 12:
            hex_string += 'c'
        elif data[i] == 13:
            hex_string += 'd'
        elif data[i] == 14:
            hex_string += 'e'
        elif data[i] == 15:
            hex_string += 'f'
        else:
            hex_string += str(data[i])
    return hex_string


#Returns the number of runs in a data set
def count_runs(flat_data):
    current_run = 0
    runs = 0
    runlength = 0
    for i in range(0, len(flat_data)):
      if i > 0:
        if current_run != flat_data[i]:
            runlength = 1
            runs += 1
            current_run = flat_data[i]
        else:
            if runlength < 15:
              runlength += 1
            else:
              runlength = 1
              runs += 1
      else:
        current_run = flat_data[i]
        runs += 1
    return runs


#Returns encoding of the raw data that is passed in
def encode_rle(flat_data):
    encoded_list = []
    current_run = 0
    run_count = 0
    for i in range(0, len(flat_data)):
        if flat_data[i] != current_run:
            if i == len(flat_data) - 1:
                    encoded_list.append(run_count)
                    encoded_list.append(current_run)
                    current_run = flat_data[i]
                    run_count = 1
                    encoded_list.append(run_count)
                    encoded_list.append(current_run)
            elif i == 0:
                current_run = flat_data[i]
                run_count += 1
            else:
                encoded_list.append(run_count)
                encoded_list.append(current_run)
                current_run = flat_data[i]
                run_count = 1
        else:
            if run_count < 15:
                if i == len(flat_data) - 1:
                      run_count += 1
                      encoded_list.append(run_count)
                      encoded_list.append(current_run)
                else:
                  run_count += 1
            else:
                  encoded_list.append(run_count)
                  encoded_list.append(current_run)
                  run_count = 1
    return encoded_list


#Returns length of decoded RLE data
def get_decoded_length(rle_data):
    decoded_list = []
    multiplier = 0
    for i in range(len(rle_data)):
        if i == 0 or i % 2 == 0:
            multiplier = rle_data[i]
        else:
            for x in range(0, multiplier):
                decoded_list.append(rle_data[i])
    return len(decoded_list)


#Returns decoded RLE data
def decode_rle(rle_data):
    decoded_list = []
    multiplier = 0
    for i in range(len(rle_data)):
        if i == 0 or i % 2 == 0:
            multiplier = rle_data[i]
        else:
            for x in range(0, multiplier):
                decoded_list.append(rle_data[i])
    return decoded_list


#Translates a string to RLE data
def string_to_data(data_string):
    data_list = []
    for i in range(len(data_string)):
        if data_string[i] == "A" or data_string[i] == "a":
            data_list.append(10)
        elif data_string[i] == "B" or data_string[i] == "b":
            data_list.append(11)
        elif data_string[i] == "C" or data_string[i] == "c":
            data_list.append(12)
        elif data_string[i] == "D" or data_string[i] == "d":
            data_list.append(13)
        elif data_string[i] == "E" or data_string[i] == "e":
            data_list.append(14)
        elif data_string[i] == "F" or data_string[i] == "f":
            data_list.append(15)
        else:
            data_list.append(int(data_string[i]))
    return data_list


#Translates RLE data into a human-readable representation. For each run, in order, it should display the run length in
#decimal (1-2 digits); the run value in hexadecimal (1 digit); and a delimiter, ‘:’, between runs. (See examples in
# standalone section.)


def to_rle_string(rle_data):
    rle_string  = ""
    for i in range(len(rle_data)):
        if i % 2 == 0 or i == 0:
            rle_string += str(rle_data[i])
        else:
            if rle_data[i] == 10:
                rle_string += 'a'
                rle_string += ':'
            elif rle_data[i] == 11:
                rle_string += 'b'
                rle_string += ':'
            elif rle_data[i] == 12:
                rle_string += 'c'
                rle_string += ':'
            elif rle_data[i] == 13:
                rle_string += 'd'
                rle_string += ':'
            elif rle_data[i] == 14:
                rle_string += 'e'
                rle_string += ':'
            elif rle_data[i] == 15:
                rle_string += 'f'
                rle_string += ':'
            else:
                rle_string += str(rle_data[i])
                rle_string += ':'
    rle_string = rle_string[:-1]
    return rle_string


#Research for the function (Split and Slicing)
#Struggled a bit as I was having a hard time appending double digit numbers
#https://www.w3schools.com/python/ref_string_split.asp
#https://www.w3schools.com/python/python_strings_slicing.asp
#https://blog.finxter.com/how-to-convert-hex-string-to-integer-in-python/
#Translates a string in human-readable RLE format (with delimiters) into RLE byte data.
def string_to_rle(rle_string):
    rle_data = []
    rle_split = rle_string.split(":")
    for i in rle_split:
        run = int(i[0:-1])
        rle_data.append(run)
        value = int(i[-1], 16) #conv    erts letters to integers
        rle_data.append(value)
    return rle_data


if __name__ == "__main__":
    main()