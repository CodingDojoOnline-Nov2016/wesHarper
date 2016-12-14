# Given the following list:

# students = [ 
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# Create a program that outputs:

# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

students = [ 
	{'first_name':  'Michael', 'last_name' : 'Jordan'},
	{'first_name' : 'John', 'last_name' : 'Rosales'},
	{'first_name' : 'Mark', 'last_name' : 'Guillen'},
	{'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def print_full_names(a_list):
	for student in students:
		print student['first_name'], student['last_name']

print_full_names(students)

# Part II -- OPTIONAL

# Now, given the following dictionary:

# users = {
#  'Students': [ 
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
#   ],
#  'Instructors': [
#      {'first_name' : 'Michael', 'last_name' : 'Choi'},
#      {'first_name' : 'Martin', 'last_name' : 'Puryear'}
#   ]
#  }
# Create a program that prints  the following format (including number of characters in each combined name):

# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13

users = {
	'Students': [ 
		{'first_name':  'Michael', 'last_name' : 'Jordan'},
		{'first_name' : 'John', 'last_name' : 'Rosales'},
		{'first_name' : 'Mark', 'last_name' : 'Guillen'},
		{'first_name' : 'KB', 'last_name' : 'Tonel'}
	],
	'Instructors': [
		{'first_name' : 'Michael', 'last_name' : 'Choi'},
		{'first_name' : 'Martin', 'last_name' : 'Puryear'}
	]
}

def print_names_and_length(a_dict):
	length = 0
	for key, data in users.items():
		for num in range(len(data)):
			if(num == 0):
				print key
			length = len(data[num]['first_name']) + len(data[num]['last_name'])
			print str(num + 1), "-", data[num]['first_name'].upper(), data[num]['last_name'].upper(), "-", str(length)

print_names_and_length(users)