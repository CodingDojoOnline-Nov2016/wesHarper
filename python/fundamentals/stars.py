# Create a function called  draw_stars() that takes a list of numbers and prints out  *.

# For example:

# x = [4, 6, 1, 3, 5, 7, 25]
# draw_stars(x) should print the following in when invoked:

# **** 
# ****** 
# * 
# *** 
# ***** 
# ******* 
# *************************
# Part 2
# Modify the function above. Allow a list containing integers and strings to be passed to the  draw_stars() function. 
# When a string is passed, instead of  displaying *, display the first letter of the string according to the example below. 
# You may use the .lower() string method for this part.
# For example:

#  x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
# draw_stars(x) should print the following in the terminal:

# **** 
# ttt 
# * 
# mmmmmmm 
# ***** 
# ******* 
# jjjjjjjjjjj



def draw_stars(a_list):
	for ele in a_list:
		print "*" * ele

list1 = [4, 6, 1, 5, 7, 25]
draw_stars(list1)


def draw_chars(a_list):
	for ele in a_list:
		if type(ele) is int:
			print "*" * ele
		elif type(ele) is float:
			round(ele)
			print "*" * ele
		else:
			print ele[0].lower() * len(ele)

list2 = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_chars(list2)