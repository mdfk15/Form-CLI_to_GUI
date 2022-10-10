#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  Copyright 2022 mdfk <mdfk@Elite>

# Libraries
import tkinter as tk

# Functions
def verify(dato):
	while dato == "":
		dato = "Error"
	return dato

def convert(value):
	while value.isdecimal() == False:
		value = input("Try again: ")
	return value

def show_students(students):
	if students:
		print(f"\nStudents list: ")
		for name,courses in students.items():
			print(f"{name} - {courses} courses")
	else:
		print("Student does not exist in DB")

# TKinter function
def clic(key):
	if key == "list":
		show_students(students)
	elif key == "add":
		name_student = verify(name.get())
		curso_student = verify(courses.get())
		if name_student == "Error":
			print("Error")
		else:
			students[name_student] = curso_student
			print("Student successfully entered.")
	elif key == "courses":
		name_student = verify(name.get())
		print(name_student)
		if name_student == "Error":
			print("Error")
		elif name_student in students:
			print(f"{name_student} - {students[name_student]} courses")
		else:
			print("Student not found")

# Data modeling.
students = {"Romina":"5","Pedro":"3","Josefa":"13"}

# Window para contener la calculadora
window = tk.Tk()
window.title("Courses form")
window.config(width=350, height=290, bg="Light Steel Blue")
window.resizable(0,0)

label = tk.Label(text="Alumni - Python project", bg="Light Steel Blue")
label.place(x=85,y=20)

# Values
width = 16
height = 2

# Botones
button = tk.Button(text="Show studens list", width=width, height=height, command=lambda:clic("list"))
button.place(x=15, y=70)

button = tk.Button(text="Add student to list", width=width, height=height, command=lambda:clic("add"))
button.place(x=15, y=220)

button = tk.Button(text="Search student in list", width=width, height=height, command=lambda:clic("courses"))
button.place(x=180, y=220)

# Input
name = tk.Entry()
name.place(x=135,y=137,width=195,height=25)
label = tk.Label(text="Nombre y apellido: ", bg="Light Steel Blue")
label.place(x=15,y=140)

courses = tk.Entry()
courses.place(x=135,y=167,width=100,height=25)
label = tk.Label(text="Cursos: ", bg="Light Steel Blue")
label.place(x=15,y=170)

window.mainloop()
