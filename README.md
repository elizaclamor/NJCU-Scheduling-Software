# NJCU-Scheduling-Software
This project uses sql database structures and queries in combination with python code to read students' availabilities to create a work schedule based on this. 

Tables include students and student_availability. 
The student table stores the student's id, first and last name, department that they are working in and the school class they are in. Both tables are related by student id.
The availability table is a JSON of said student's weekly availability in 24 hour time notation.

One must have mySQL connector installed to run. Note that if new students are added, all respective sql additions must be completed (eg. creating the student with an id and details and also creating availability for said student). Their availabilities must be inserted into the availability table.

