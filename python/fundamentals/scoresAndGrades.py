# Create a program that prompts the user ten times for a test score between 60 and 100. 
# Each time a score is generated, your program should display what the grade is for a particular score. 
# Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

def scores_and_grades():
	print "Scores and Grades"
	for num in range(10):
		score = int(raw_input())
		if(score >= 90):
			grade = "A"
		elif(score >= 80):
			grade = "B"
		elif(score >= 70):
			grade = "C"
		elif(score >= 60):
			grade = "D"
		else:
			grade = "... Wow, you're a terrible student, or inputted something other than a number."
		print "Score:", str(score), "Your grade is", grade
	print "End of the program. Bye!"

scores_and_grades()