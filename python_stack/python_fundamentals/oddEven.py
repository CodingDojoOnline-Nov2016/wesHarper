# Create a function that counts from 1 to 2000. As it loops through each number, have your program generate the
# number and specify whether it's an odd or even number.

def oddEven(start, end):
	for num in range(start, end + 1, 1):
		string = "Number is " + str(num) + ". This is "
		if(num % 2 == 0):
			string += "an even number."
		else:
			string += "an odd number."
		print string

oddEven(1, 2000)