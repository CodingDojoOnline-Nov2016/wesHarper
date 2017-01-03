def insert_val_at(index, my_list, value):
	if index >= len(my_list):
		return False
	my_list.append(my_list[len(my_list) - 1])
	for i in range(len(my_list) - 2, index - 1, -1):
		my_list[i + 1] = my_list[i]
	my_list[index] = value
	return my_list