# You're going to create a program that simulates tossing a coin 5,000 times. 
# Your program should display how many times the head/tail appears.

# Sample output should be like the following:

#           Starting the program...

# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far 
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far 
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far 
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ........
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far 

# Ending the program, thank you!

import random

def coin_tosses(num_tosses):
	print "Starting the program..."
	heads = 0
	tails = 0
	for num in range(num_tosses):
		result = int(round(random.random()))
		if(result is 1):
			current = "head!"
			heads += 1
		else:
			current = "tail!"
			tails += 1
		print "Attempt #" + str(num + 1) + ": Throwing a coin... It's a " + str(current) + " ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far."
	print "Ending the program, thank you!"

coin_tosses(5000)