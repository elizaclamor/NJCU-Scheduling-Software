''' Database set up for project
include tables: STUDENT, STUDENT_AVAILABILITY'''

create_database_query = "CREATE DATABASE coop_project"

create_student_table = """
CREATE TABLE student(
    id INT PRIMARY KEY,
    first_name VARCHAR(16) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    department VARCHAR(20) NOT NULL,
    class VARCHAR(10) NOT NULL
);
"""

create_student_availability_table = """
CREATE TABLE student_availability(
    id INT PRIMARY KEY,
    availability json NOT NULL, 
    week_beginning DATE NOT NULL
);
"""

alter_student_availability_fk = """
ALTER TABLE student_availability
ADD FOREIGN KEY (id) REFERENCES student(id)
"""

insert_s1 = 'INSERT INTO student(id, first_name, last_name, department, class) VALUES (001, "Vanshita", "Malhotra", "Front Desk", "Sophomore");'
insert_s2 = 'INSERT INTO student(id, first_name, last_name, department, class) VALUES (002, "Michael", "Cross", "Front Desk", "Sophomore");'
insert_s3 = 'INSERT INTO student(id, first_name, last_name, department, class) VALUES (003, "Sara", "Zorzan", "Front Desk", "Sophomore");'
insert_s4 = 'INSERT INTO student(id, first_name, last_name, department, class) VALUES (004, "Giada", "Zorzan", "Front Desk", "Junior");'
insert_s5 = 'INSERT INTO student(id, first_name, last_name, department, class) VALUES (005, "Nico", "Teynie", "Front Desk", "Senior");'
insert_s6 = 'INSERT INTO student(id, first_name, last_name, department, class) VALUES (006, "Aaron", "Mantilla", "Front Desk", "Senior");'
insert_s7 = 'INSERT INTO student(id, first_name, last_name, department, class) VALUES (007, "Priyam", "Shah", "Front Desk", "Graduate");'
insert_s8 = 'INSERT INTO student(id, first_name, last_name, department, class) VALUES (008, "Hannah", "Alvarado", "Front Desk", "Junior");'

insert_s1_avail = """INSERT INTO student_availability(id, availability, week_beginning) VALUES(001, 
    '{
    "Monday" : {
        "start" : "0600",
        "end"   : "1400"},
    "Tuesday" : {
        "start" : "null",
        "end"   : "null"},
    "Wednesday": {
        "start" : "0600",
        "end"   : "1400" },
    "Thursday" : {
        "start" : "1200",
        "end"   : "2200"},
    "Friday" : {
        "start" : "0600",
        "end"   : "1800"},
    "Saturday" : {
        "start" : "null",
        "end"   : "null"},
    "Sunday" : {
        "start" : "1000",
        "end"   : "1600"} 
    }',
    '2022-12-05');"""
insert_s2_avail = """INSERT INTO student_availability(id, availability, week_beginning) VALUES(002, 
    '{
    "Monday" : {
        "start" : "0800",
        "end"   : "1300"},
    "Tuesday" : {
        "start" : "1500",
        "end"   : "2200"},
    "Wednesday": {
        "start" : "1500",
        "end"   : "1900"},
    "Thursday" : {
        "start" : "null",
        "end"   : "null"},
    "Friday" : {
        "start" : "0800",
        "end"   : "1800"},
    "Saturday" : {
        "start" : "0700",
        "end"   : "1500"},
    "Sunday" : {
        "start" : "1200",
        "end"   : "2000"}
    }', 
    '2022-12-05');"""
insert_s3_avail = """INSERT INTO student_availability(id, availability, week_beginning) VALUES(003, 
    '{"Monday"   : {
        "start" : "null",
        "end"   : "null"},
    "Tuesday"  : {
        "start" : "0900",
        "end"   : "2200"},
    "Wednesday": {
        "start" : "1000",
        "end"   : "2000"},
    "Thursday" : {
        "start" : "0800",
        "end"   : "1400"},
    "Friday"   : {
        "start" : "1500",
        "end"   : "2300"},
    "Saturday" : {
        "start" : "0600",
        "end"   : "1300"},
    "Sunday"   : {
        "start" : "0600",
        "end"   : "1200"}
    }', '2022-12-05');"""
insert_s4_avail = """INSERT INTO student_availability(id, availability, week_beginning) VALUES(004, 
    '{"Monday"   : {
        "start" : "1300",
        "end"   : "2200"},
    "Tuesday"  : {
        "start" : "0600",
        "end"   : "1200"},
    "Wednesday": {
        "start" : "1000",
        "end"   : "1700"},
    "Thursday" : {
        "start" : "0500",
        "end"   : "1300"},
    "Friday"   : {
        "start" : "null",
        "end"   : "null"},
    "Saturday" : {
        "start" : "0700",
        "end"   : "1300"},
    "Sunday"   : {
        "start" : "null",
        "end"   : "null"}
    }', '2022-12-05');"""
insert_s5_avail = """INSERT INTO student_availability(id, availability, week_beginning) VALUES(005, 
    '{"Monday"   : {
        "start" : "0600",
        "end"   : "1800"},
    "Tuesday"  : {
        "start" : "1000",
        "end"   : "1500"},
    "Wednesday": {
        "start" : "1300",
        "end"   : "2200"},
    "Thursday" : {
        "start" : "null",
        "end"   : "null"},
    "Friday"   : {
        "start" : "null",
        "end"   : "null"},
    "Saturday" : {
        "start" : "null",
        "end"   : "null"},
    "Sunday"   : {
        "start" : "null",
        "end"   : "null"}
    }', '2022-12-05');"""
insert_s6_avail = """INSERT INTO student_availability(id, availability, week_beginning) VALUES(006, 
    '{"Monday"   : {
        "start" : "1700",
        "end"   : "2200"},
    "Tuesday"  : {
        "start" : "0600",
        "end"   : "1800"},
    "Wednesday": {
        "start" : "0600",
        "end"   : "1400"},
    "Thursday" : {
        "start" : "1300",
        "end"   : "2200"},
    "Friday"   : {
        "start" : "0600",
        "end"   : "1800"},
    "Saturday" : {
        "start" : "0700",
        "end"   : "1700"},
    "Sunday"   : {
        "start" : "0700",
        "end"   : "1700"}
    }', '2022-12-05');"""
insert_s7_avail = """INSERT INTO student_availability(id, availability, week_beginning) VALUES(007, 
    '{"Monday"   : {
        "start" : "0600",
        "end"   : "1500"},
    "Tuesday"  : {
        "start" : "1300",
        "end"   : "2300"},
    "Wednesday": {
        "start" : "1300",
        "end"   : "2300"},
    "Thursday" : {
        "start" : "1300",
        "end"   : "2300"},
    "Friday"   : {
        "start" : "1700",
        "end"   : "2300"},
    "Saturday" : {
        "start" : "null",
        "end"   : "null"},
    "Sunday"   : {
        "start" : "0700",
        "end"   : "1200"}
    }', '2022-12-05');"""
insert_s8_avail = """INSERT INTO student_availability(id, availability, week_beginning) VALUES(008, 
    '{"Monday"   : {
        "start" : "1800",
        "end"   : "2300"},
    "Tuesday"  : {
        "start" : "1000",
        "end"   : "1400"},
    "Wednesday": {
        "start" : "0600",
        "end"   : "1400"},
    "Thursday" : {
        "start" : "0600",
        "end"   : "1800"},
    "Friday"   : {
        "start" : "1300",
        "end"   : "2200"},
    "Saturday" : {
        "start" : "0700",
        "end"   : "1200"},
    "Sunday"   : {
        "start" : "1200",
        "end"   : "1700"}
    }', '2022-12-05');"""

