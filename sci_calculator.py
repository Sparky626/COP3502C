import math



def calculator():
    result = 0.0
    sumOfCalc = 0.0
    numOfCalc = 0.0
    avgofCalc = 0.0
    continuing = True
    print("Current Result: " + str(result))
    menu()
    while continuing == True:
        sumOfCalc += float(result)
        operation = int(input("Enter Menu Selection: "))
        if operation == 0:
            continuing = False
            print("Thanks for using this calculator. Goodbye!")
        elif operation == 1:
            foperand = input("Enter first operand: ")
            soperand = input("Enter second operand: ")
            if foperand == "RESULT":
                foperand = result
            if soperand == "RESULT":
                soperand = result
            print(" ")
            result = float(foperand) + float(soperand)
            print("Current Result: " + str(result))
            menu()
            numOfCalc += 1
        elif operation == 2:
            foperand = input("Enter first operand: ")
            soperand = input("Enter second operand: ")
            if foperand == "RESULT":
                foperand = result
            if soperand == "RESULT":
                soperand = result
            print(" ")
            result = float(foperand) - float(soperand)
            print("Current Result: " + str(result))
            menu()
            numOfCalc += 1
        elif operation == 3:
            foperand = input("Enter first operand: ")
            soperand = input("Enter second operand: ")
            if foperand == "RESULT":
                foperand = result
            if soperand == "RESULT":
                soperand = result
            print(" ")
            result = float(foperand) * float(soperand)
            print("Current Result: " + str(result))
            menu()
            numOfCalc += 1
        elif operation == 4:
            foperand = input("Enter first operand: ")
            soperand = input("Enter second operand: ")
            if foperand == "RESULT":
                foperand = result
            if soperand == "RESULT":
                soperand = result
            print(" ")
            result = float(foperand) / float(soperand)
            print("Current Result: " + str(result))
            menu()
            numOfCalc += 1
        elif operation == 5:
            foperand = input("Enter first operand: ")
            soperand = input("Enter second operand: ")
            if foperand == "RESULT":
                foperand = result
            if soperand == "RESULT":
                soperand = result
            print(" ")
            result = float(foperand)**float(soperand)
            print("Current Result: " + str(result))
            menu()
            numOfCalc += 1
        elif operation == 6:
            foperand = input("Enter first operand: ")
            soperand = input("Enter second operand: ")
            if foperand == "RESULT":
                foperand = result
            if soperand == "RESULT":
                soperand = result
            print(" ")
            result = math.log(float(soperand),float(foperand))
            print("Current Result: " + str(result))
            menu()
            numOfCalc += 1
        elif operation == 7:
            if numOfCalc == 0:
                print(" ")
                print("Error: No calculations yet to average!")
                print(" ")
            else:
                avgofCalc = round(sumOfCalc/numOfCalc,2)
                print(" ")
                print("Sum of calculations: " + str(sumOfCalc))
                print("Number of calculations: " + str(int(numOfCalc)))
                print("Average of calculations: " + str(avgofCalc))
        else:
            print("Error: Invalid selection!")
def menu():
    print(" ")
    print("Calculator Menu")
    print("---------------")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print('7. Display Average')
    print(" ")
    
calculator()
