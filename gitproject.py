def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode():
    password = input("Please enter your password to encode: ")
    new_password = ""
    for i in range(0, len(password)):
        int_changer = int(password[i])
        int_changer += 3
        new_password += str(int_changer)
    print("Your password has been encoded and stored!")
    print(" ")
    return new_password


def decode(password):
    old_password = ""
    for i in range(0, len(password)):
        int_changer = int(password[i])
        int_changer -= 3
        old_password += str(int_changer)
    print("The encoded password is " + password + ", and the original password is " + old_password + ".")


def main():
    menu()
    password = None
    program_active = True
    while program_active:
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = encode()
        elif choice == 2:
            decode(password)
        else:
            program_active = False


if __name__ == "__main__":
    main()

