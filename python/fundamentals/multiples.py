# Create a program that prints all the odd numbers from 1 to 1000. Use the for loop and don't use array to do this exercise.

for num in range(1, 1001):
	print num

# Create another program that prints all the multiples of 5 from 5 to 1,000,000.

for num in range(0, 1000001, 5):
	print num

# Less efficient, but useful to know for later
# for num in range(1000001):
# 	if(num % 5 == 0):
# 		print num