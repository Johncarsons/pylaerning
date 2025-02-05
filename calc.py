num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operator:(+,-,*,/) ")

# perform the calculation based on the operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = " ERROR! Cannot divide by zero"
else:
    result = "INVALID OPERATOR"
print(f"The result is: {result}")

