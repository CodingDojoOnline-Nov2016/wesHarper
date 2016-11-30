# Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16]) and returns a list
# where each value has been multiplied by 5. For example: b = multiply(a, 5); print b; should print [10, 20, 50, 80].

a = [2, 4, 10, 16]

def multiply(li, mult):
	for i in range(len(li)):
		li[i] *= mult
	return li

b = multiply(a, 5)
print b