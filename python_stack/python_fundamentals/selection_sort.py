def selection_sort(a_list):
	min_start = 0
	max_start = len(a_list) - 1
	while min_start < len(a_list):
		for num in range(min_start, len(a_list) - 1 / 2):
			if a_list[num] < a_list[min_start]:
				a_list[num], a_list[min_start] = a_list[min_start], a_list[num]
		for num in range(max_start, len(a_list) - 1 / 2, -1):
			if a_list[num] > a_list[max_start]:
				a_list[num], a_list[max_start] = a_list[max_start], a_list[num]		
		min_start += 1
		max_start -= 1
	return a_list

import random

list1 = [8, 6, 2, 1, 0, 9, 3, 7, 4, 5, 10]
list2 = [random.randint(0, 10000) for count in range(100)]

print selection_sort(list1)
print selection_sort(list2)