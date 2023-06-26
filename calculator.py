foperand = float(input("Enter first operand: "))
soperand = float(input("Enter second operand: "))

print("Calculator Menu")
print("---------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

#try:
#    operation = int(input("Which operation do you want to perform? "))
#except ValueError:
#    print("Error: Invalid selection! terminating program.")
operation = int(input("Which operation do you want to perform? "))
if operation == 1:
    result = str(foperand + soperand)
    print("The result of the operation is " + result + ". Goodbye!")
elif operation == 2:
    result = str(foperand - soperand)
    print("The result of the operation is " + result + ". Goodbye!")
elif operation == 3:
    result = str(foperand * soperand)
    print("The result of the operation is " + result + ". Goodbye!")
elif operation == 4:
    result = str(foperand / soperand)
    print("The result of the operation is " + result + ". Goodbye!")
else:
    print("Error: Invalid selection! Terminating program.")
