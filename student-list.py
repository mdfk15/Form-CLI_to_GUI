#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  Copyright 2022 mdfk <mdfk@Elite>

# Functions
def verify(dato):
	while dato == "":
		print("Error")
		dato = input("Try again: ")
	return dato

def convert(value):
	while value.isdecimal() == False:
		print("Error")
		value = input("Try again: ")
	return value

# Create empty dicctionaire.
students = {}

# Main menu
menu = """
     Option menu
----------------------
1 - Show student list
2 - Enter student
3 - Search student
4 - Exit
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
			courses = students[student]
			# I need to define the varible "courses" 
			# to concatenate it  with another variable or string
			print(student + " - " + str(courses) + " courses")
	elif option == "2":
		name_student = input("Enter the student name: ")
		name_sturent = verify(name_student)
		# Here we need to define it as "int" 
		# since input() always return a "string"
		courses = input("Enter number of courses: ")
		courses = convert(courses)
		students[name_student] = courses
		print("Student successfully entered.")
	elif option == "3":
		name_student = input("Enter the student name: ")
		if name_student in students:
			print(name_student +" have "+ str(students[name_student])+" courses")
		else:
			print("Student does not exist in DB'")
	elif option == "4":
		# Break loop.
		break
	else:
		print("Incorrect option, try again.")
print("¡Thanks You for using this program!")
