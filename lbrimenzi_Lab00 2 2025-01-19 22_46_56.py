# This function takes 2 numbers, then it adds them, then returns the result
def add(first_number, second_number):
	return first_number + second_number
# I call the function here. It will print whatever the function returns
print("74 + 23 = ", add(74,23))

# This function takes 2 numbers, then subtracts the second from the first
def subtract(first_number, second_number):
	return first_number - second_number

# I call the subtract function here. 
print("74 - 23 = ", subtract(74,23))

# This function takes 2 numbers and multiplies them
def multiply(first_number,second_number):
	return first_number * second_number

# I call the multiply function here
print("74 * 23 ", multiply(74,23))

# This function takes 2 numbers and divides the first by the second
def divide(first_number,second_number):
	return first_number / second_number

# I call the divide function here
print("74 / 23 ", divide(74,23.))

# This will pause the code until the user enters 2 numbers and hits enter
firstNum = input("Enter the first number")
secondNum = input("Enter the second number")
operator = input("Do you want to add, subtract, multiply, or divide?")

# Check to see which function to call

if operator == "+":
	print(add(firstNum, secondNum))
elif operator == "-":
	print(subtract(firstNum, secondNum))
elif operator == "*":
	print(multiply(firstNum, secondNum))
elif operator == "/":
	print(divide(firstNum, secondNum))
else: 
	print("You picked the wrong operator please pick either +,-,/, or *")

