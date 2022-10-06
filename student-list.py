#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  Copyright 2022 mdfk <mdfk@Elite>

# Create empty list.
students = []

# Main menu
menu = """
     Option menu
----------------------
1 - Show student list
2 - Enter student
3 - Exit
"""

# Menu loop (only exit with "3" option).
while True:
	print(menu)
	
	option = input("Enter the Option: ")
	if option == "1":
		print(f"\nStudent list:")
		for student in students:
			# I take each element in list students
			# At the same time each element is a list
			# The first element is the name and the second is the number of courses.
			name = student[0]
			courses = student[1]
			# I need to define the varible "courses" 
			# to concatenate it  with another variable or string
			print(name + " - " + str(courses) + " courses")
	elif option == "2":
		name_student = input("Enter the student name: ")
		# Here we need to define it as "int" 
		# since input() always return a "string"
		courses = int(input("Enter number of courses: "))
		if name_student == "":
			print("Error: name no entered.")
		else:
			# Enter variables in list
			students.append([name_student, courses])
			print("Student successfully entered.")
	elif option == "3":
		# Break loop.
		break
	else:
		print("Incorrect option, try again.")
print("¡Thanks You for using this program!")
