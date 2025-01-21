# This function takes 2 numbers, then it adds them, then returns the result
def add(first_number, second_number):
	return first_number + second_number
# I call the function here. It will print whatever the function returns
#print("74 + 23 = ", add(74,23))

# This function takes 2 numbers, then subtracts the second from the first
def subtract(first_number, second_number):
	return first_number - second_number

# I call the subtract function here. 
#print("74 - 23 = ", subtract(74,23))

# This function takes 2 numbers and multiplies them
def multiply(first_number,second_number):
	return first_number * second_number

# I call the multiply function here
#print("74 * 23 ", multiply(74,23))

# This function takes 2 numbers and divides the first by the second
def divide(first_number,second_number):
	return first_number / second_number

### progtam code

print("To end the program use KeyboardInterrupt aka ctrl+C")
# I call the divide function here
#print("74 / 23 ", divide(74,23.))
firstNumFlag = False
secondNumFlag = False
operatorFlag = False
try:
	while True:
		#firstNum loop
		while not firstNumFlag:
				#this will pause the code until the user enters 2 numbers
			firstNum = input("Enter the first number. It must be a number: ")
			try:
				firstNum = float(firstNum)
				firstNumFlag = True
			except  ValueError:
				print("This is not a number. Please retry.")
				continue
			'''  "continue" re-enters loop without updating flag 
			to True or executing any othe code
		#	firstNum = input("Enter the first number. It must be a number.")
		#if type(firstNum) != "float":
		#	print("This is not a number. Please retry.")
		'''
			while not secondNumFlag:
				secondNum = input("Enter the second number. It must be a number: ")
				try:
					secondNum = float(secondNum)
					secondNumFlag = True
				except ValueError:
					print("This is not a number. Please retry.")
					continue 
		#re-enters loop without updating the flag to True or False
		while not operatorFlag:
			operator = input("Do you want to add, subtract, multiply, or divide? Type +, -, *, or /: ")
				#check to that the operator is valid
			operatorFlag = (operator == "+") or (operator == "-") or (operator == "*") or (operator == "/")
			#print("operatorFlag = ", operatorFlag)
				#checking if it worked
				#Checking wether the user wants to divide by zero (this wont work)
			if(operator =="/" and secondNum==0):
				print("You are unable to divide by zero please try new numbers")
				secondNumFlag = False
				operatorFlag = False
				continue
				#loop again 

		# After getting here check to see which function to call		

		if operator == "+":
			print(add(firstNum, secondNum))
		elif operator == "-":
			print(subtract(firstNum, secondNum))
		elif operator == "*":
			print(multiply(firstNum, secondNum))
		elif operator == "/":
			print(divide(firstNum, secondNum))
		#reseting Flags 
		firstNumFlag = False
		secondNumFlag = False
		operatorFlag = False
except KeyboardInterrupt:
	#print it on a new lin
	print("\nWe are done now")
