# project main file

# imports
import mysql.connector
from mysql.connector import Error
from database import *
from queries import *
import random

# connect to the database (requires db password)
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# create database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

# create connection
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# run queries
def execute_query(connection, query, multitf):
    cursor = connection.cursor()
    try:
        cursor.execute(query, multi=multitf)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


# read queries 
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

# creates arrays from the data returned
def create_list_from_data(list_name, results):
    for id in results:
        # results are returned in a bracketed format, this is eliminated here
        split = [*id]
        list_name.append(split[0])

# picks a worker for the shift using random 
def pick_shift(available_students):
    return random.choice(available_students)

# create a dictionary to identify the names from the student worker id
def create_student_dict(dict_name, results):
    # identify key as id and value as full name
    for item in results:
        name = item[1] + " " + item[2]
        dict_name[item[0]] = name 
    
    return dict_name


# Can move this section later to a different file for tidiness
# testing validity
pw = "Youwillbe0kay!"
connection = create_server_connection("localhost", "root", pw)

# create database
# create_database(connection, create_database_query)
db = 'coop_project'
connection = create_db_connection("localhost", "root", pw, db)

# create tables
execute_query(connection, create_student_table, False)
execute_query(connection, create_student_availability_table, False)
execute_query(connection, alter_student_availability_fk, False)

# populate student table
execute_query(connection, insert_s1, False)
execute_query(connection, insert_s2, False)
execute_query(connection, insert_s3, False)
execute_query(connection, insert_s4, False)
execute_query(connection, insert_s5, False)
execute_query(connection, insert_s6, False)
execute_query(connection, insert_s7, False)
execute_query(connection, insert_s8, False)

# populate student availability table
execute_query(connection, insert_s1_avail, False)
execute_query(connection, insert_s2_avail, False)
execute_query(connection, insert_s3_avail, False)
execute_query(connection, insert_s4_avail, False)
execute_query(connection, insert_s5_avail, False)
execute_query(connection, insert_s6_avail, False)
execute_query(connection, insert_s7_avail, False)
execute_query(connection, insert_s8_avail, False)

# retreiving those who are available to work the shift

# monday shifts
m1_array = read_query(connection, m_first_shift_avail)
m2_array = read_query(connection, m_second_shift_avail)
m3_array = read_query(connection, m_third_shift_avail)
m4_array = read_query(connection, m_fourth_shift_avail)

# tuesday shifts
t1_array = read_query(connection, t_first_shift_avail)
t2_array = read_query(connection, t_second_shift_avail)
t3_array = read_query(connection, t_third_shift_avail)
t4_array = read_query(connection, t_fourth_shift_avail)

# wednesday shifts 
w1_array = read_query(connection, w_first_shift_avail)
w2_array = read_query(connection, w_second_shift_avail)
w3_array = read_query(connection, w_third_shift_avail)
w4_array = read_query(connection, w_fourth_shift_avail)

# thursday shifts
th1_array = read_query(connection, th_first_shift_avail)
th2_array = read_query(connection, th_second_shift_avail)
th3_array = read_query(connection, th_third_shift_avail)
th4_array = read_query(connection, th_fourth_shift_avail)

# friday shifts
f1_array = read_query(connection, f_first_shift_avail)
f2_array = read_query(connection, f_second_shift_avail)
f3_array = read_query(connection, f_third_shift_avail)
f4_array = read_query(connection, f_fourth_shift_avail)

# saturday shifts
s1_array = read_query(connection, s_first_shift_avail)
s2_array = read_query(connection, s_second_shift_avail)

# sunday shifts
su1_array = read_query(connection, su_first_shift_avail)
su2_array = read_query(connection, su_second_shift_avail)


# empty lists to store available ids
m1, m2, m3, m4 = [],[],[],[]
t1, t2, t3, t4 = [],[],[],[]
w1, w2, w3, w4 = [],[],[],[]
th1, th2, th3, th4 = [],[],[],[]
f1, f2, f3, f4 = [],[],[],[]
s1, s2= [],[]
su1, su2 = [],[]

# run through for loop from query of return and store names in array
create_list_from_data(m1, m1_array)
create_list_from_data(m2, m2_array)
create_list_from_data(m3, m3_array)
create_list_from_data(m4, m4_array)

create_list_from_data(t1, t1_array)
create_list_from_data(t2, t2_array)
create_list_from_data(t3, t3_array)
create_list_from_data(t4, t4_array)

create_list_from_data(w1, w1_array)
create_list_from_data(w2, w2_array)
create_list_from_data(w3, w3_array)
create_list_from_data(w4, w4_array)

create_list_from_data(th1, th1_array)
create_list_from_data(th2, th2_array)
create_list_from_data(th3, th3_array)
create_list_from_data(th4, th4_array)

create_list_from_data(f1, f1_array)
create_list_from_data(f2, f2_array)
create_list_from_data(f3, f3_array)
create_list_from_data(f4, f4_array)

create_list_from_data(s1, s1_array)
create_list_from_data(s2, s2_array)

create_list_from_data(su1, su1_array)
create_list_from_data(su2, su2_array)


# algorithm to randomly choose individual to work
# use rand to select a name 

# shifts totals
week = 7
weekday_shifts = 4
weekend_shifts = 2

total_shifts = (5 * weekday_shifts) + (2 * weekend_shifts)

# picking workers for shifts
m1_worker = pick_shift(m1)
m2_worker = pick_shift(m2)
m3_worker = pick_shift(m3)
m4_worker = pick_shift(m4)

t1_worker = pick_shift(t1)
t2_worker = pick_shift(t2)
t3_worker = pick_shift(t3)
t4_worker = pick_shift(t4)

w1_worker = pick_shift(w1)
w2_worker = pick_shift(w2)
w3_worker = pick_shift(w3)
w4_worker = pick_shift(w4)

th1_worker = pick_shift(th1)
th2_worker = pick_shift(th2)
th3_worker = pick_shift(th3)
th4_worker = pick_shift(th4)

f1_worker = pick_shift(f1)
f2_worker = pick_shift(f2)
f3_worker = pick_shift(f3)
f4_worker = pick_shift(f4)

s1_worker = pick_shift(s1)
s2_worker = pick_shift(s2)

su1_worker = pick_shift(s1)
su2_worker = pick_shift(s2)

# once schedule is generated, go through schedule and check if individual is working twice in the same day
# if they are not working the day already or are working the shift before or after. 
schedule = {}

schedule[0] = [m1_worker, '6am-10am']
schedule[1] = [m2_worker, '10am-2pm']
schedule[2] = [m3_worker, '2pm-6pm']
schedule[3] = [m4_worker, '6pm-10pm']

schedule[4] = [t1_worker, '6am-10am']
schedule[5] = [t2_worker, '10am-2pm']
schedule[6] = [t3_worker, '2pm-6pm']
schedule[7] = [t4_worker, '6pm-10pm']

schedule[8] = [w1_worker, '6am-10am']
schedule[9] = [w2_worker, '10am-2pm']
schedule[10] = [w3_worker, '2pm-6pm']
schedule[11] = [w4_worker, '6pm-10pm']

schedule[12] = [th1_worker, '6am-10am']
schedule[13] = [th2_worker, '10am-2pm']
schedule[14] = [th3_worker, '2pm-6pm']
schedule[15] = [th4_worker, '6pm-10pm']

schedule[16] = [f1_worker, '6am-10am']
schedule[17] = [f2_worker, '10am-2pm']
schedule[18] = [f3_worker, '2pm-6pm']
schedule[19] = [f4_worker, '6pm-10pm']

schedule[20] = [s1_worker, '7am-12pm']
schedule[21] = [s2_worker, '12pm-5pm']

schedule[22] = [su1_worker, '7am-12pm']
schedule[23] = [su2_worker, '12pm-5pm']

# create dictionary of names and worker ID
names_results = read_query(connection, get_names)
id_to_name = {}
create_student_dict(id_to_name, names_results)

# change workers to names by for loop going through list 
for i in range(total_shifts):
    for id in id_to_name:
        if schedule[i][0] == id:
            schedule[i][0] = id_to_name[id]

# create file that shows the schedule
# in print schedule file

# get date for the schedule
date = read_query(connection, get_week)
