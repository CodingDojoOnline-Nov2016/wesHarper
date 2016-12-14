def bubble_sort(a_list):
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(a_list) - 1):
			if a_list[i] > a_list[i + 1]:
				a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i] #tuple unpacking
				swapped = True
	return a_list

unsorted = [6, 1, 8, 3, 5, 7, 4, 2]

import random

unsorted2 = [random.randint(0, 10000) for count in range(100)]

print bubble_sort(unsorted)
print bubble_sort(unsorted2)