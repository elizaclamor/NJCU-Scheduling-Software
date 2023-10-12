''' Queries for the project 

SHIFTS
MTWThF: 6-10, 10-2, 2-6, 6-10
SSu: 7-12, 12-5
'''

# these shifts are hard coded 
# returns id that is available for the shift
m_first_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Monday.start") AS DECIMAL) <= 600
AND CAST(JSON_EXTRACT(availability, "$.Monday.end") AS DECIMAL) >= 1000;
"""
t_first_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Tuesday.start") AS DECIMAL) <= 600
AND CAST(JSON_EXTRACT(availability, "$.Tuesday.end") AS DECIMAL) >= 1000;
"""
w_first_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Wednesday.start") AS DECIMAL) <= 600
AND CAST(JSON_EXTRACT(availability, "$.Wednesday.end") AS DECIMAL) >= 1000;
"""
th_first_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Thursday.start") AS DECIMAL) <= 600
AND CAST(JSON_EXTRACT(availability, "$.Thursday.end") AS DECIMAL) >= 1000;
"""
f_first_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Friday.start") AS DECIMAL) <= 600
AND CAST(JSON_EXTRACT(availability, "$.Friday.end") AS DECIMAL) >= 1000;
"""
s_first_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Saturday.start") AS DECIMAL) <= 700
AND CAST(JSON_EXTRACT(availability, "$.Saturday.end") AS DECIMAL) >= 1200;
"""
su_first_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Sunday.start") AS DECIMAL) <= 700
AND CAST(JSON_EXTRACT(availability, "$.Sunday.end") AS DECIMAL) >= 1200;
"""

m_second_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Monday.start") AS DECIMAL) <= 1000
AND CAST(JSON_EXTRACT(availability, "$.Monday.end") AS DECIMAL) >= 1400;
"""
t_second_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Tuesday.start") AS DECIMAL) <= 1000
AND CAST(JSON_EXTRACT(availability, "$.Tuesday.end") AS DECIMAL) >= 1400;
"""
w_second_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Wednesday.start") AS DECIMAL) <= 1000
AND CAST(JSON_EXTRACT(availability, "$.Wednesday.end") AS DECIMAL) >= 1400;
"""
th_second_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Thursday.start") AS DECIMAL) <= 1000
AND CAST(JSON_EXTRACT(availability, "$.Thursday.end") AS DECIMAL) >= 1400;
"""
f_second_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Friday.start") AS DECIMAL) <= 1000
AND CAST(JSON_EXTRACT(availability, "$.Friday.end") AS DECIMAL) >= 1400;
"""
s_second_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Saturday.start") AS DECIMAL) <= 1200
AND CAST(JSON_EXTRACT(availability, "$.Saturday.end") AS DECIMAL) >= 1700;
"""
su_second_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Sunday.start") AS DECIMAL) <= 1200
AND CAST(JSON_EXTRACT(availability, "$.Sunday.end") AS DECIMAL) >= 1700;
"""

m_third_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Monday.start") AS DECIMAL) <= 1400
AND CAST(JSON_EXTRACT(availability, "$.Monday.end") AS DECIMAL) >= 1800;
"""
t_third_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Tuesday.start") AS DECIMAL) <= 1400
AND CAST(JSON_EXTRACT(availability, "$.Tuesday.end") AS DECIMAL) >= 1800;
"""
w_third_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Wednesday.start") AS DECIMAL) <= 1400
AND CAST(JSON_EXTRACT(availability, "$.Wednesday.end") AS DECIMAL) >= 1800;
"""
th_third_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Thursday.start") AS DECIMAL) <= 1400
AND CAST(JSON_EXTRACT(availability, "$.Thursday.end") AS DECIMAL) >= 1800;
"""
f_third_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Friday.start") AS DECIMAL) <= 1400
AND CAST(JSON_EXTRACT(availability, "$.Friday.end") AS DECIMAL) >= 1800;
"""

m_fourth_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Monday.start") AS DECIMAL) <= 1800
AND CAST(JSON_EXTRACT(availability, "$.Monday.end") AS DECIMAL) >= 2200;
"""
t_fourth_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Tuesday.start") AS DECIMAL) <= 1800
AND CAST(JSON_EXTRACT(availability, "$.Tuesday.end") AS DECIMAL) >= 2200;
"""
w_fourth_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Wednesday.start") AS DECIMAL) <= 1800
AND CAST(JSON_EXTRACT(availability, "$.Wednesday.end") AS DECIMAL) >= 2200;
"""
th_fourth_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Thursday.start") AS DECIMAL) <= 1800
AND CAST(JSON_EXTRACT(availability, "$.Thursday.end") AS DECIMAL) >= 2200;
"""
f_fourth_shift_avail = """
SELECT ID
FROM student_availability
WHERE CAST(JSON_EXTRACT(availability, "$.Friday.start") AS DECIMAL) <= 1800
AND CAST(JSON_EXTRACT(availability, "$.Friday.end") AS DECIMAL) >= 2200;
"""

get_names = """
SELECT id, 
    first_name, 
    last_name
FROM student
"""

get_week = """
SELECT DATE_FORMAT(week_beginning, '%Y-%m-%d') as date
FROM student_availability
GROUP BY 1;
"""
