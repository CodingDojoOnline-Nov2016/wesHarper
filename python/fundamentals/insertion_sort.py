def insertion_sort(a_list):
	index = 1
	while index < len(a_list):
		insertion_idx = index
		for num in range(index, 0 - 1, -1):
			if a_list[num] > a_list[index]:
				insertion_idx = num
		for num in range(index, insertion_idx, -1):
			a_list[num], a_list[num - 1] = a_list[num - 1], a_list[num]
		index += 1
	return a_list

import random

list1 = [6, 3, 4, 5, 9, 10, 2, 7, 8, 1, 0]
list2 = [random.randint(0, 10000) for count in range(100)]

print insertion_sort(list1)
print insertion_sort(list2)