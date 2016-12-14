# Create a program that prints the average of the values in the list:

a = [1, 2, 5, 10, 255, 3]
avg = 0

for ele in a:
	avg += ele / len(a)

print avg