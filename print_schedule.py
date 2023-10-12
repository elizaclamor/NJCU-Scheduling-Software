''' 
Function to create file for schedule in easily readable format
'''

# imports
from project import *
from prettytable import PrettyTable

schedule_file = open("schedulefile.txt", "w")
schedule_file.write("Week Beginning : {} \n".format(date[0][0]))

# creating pretty table
schedule_table = PrettyTable(["Shift Time", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
schedule_table.add_row([schedule[0][1], schedule[0][0], schedule[4][0], schedule[8][0], schedule[12][0], schedule[16][0], "-", "-"])
schedule_table.add_row([schedule[1][1], schedule[1][0], schedule[5][0], schedule[9][0], schedule[13][0], schedule[17][0], "-", "-"])
schedule_table.add_row([schedule[2][1], schedule[2][0], schedule[6][0], schedule[10][0], schedule[14][0], schedule[18][0], "-", "-"])
schedule_table.add_row([schedule[3][1], schedule[3][0], schedule[7][0], schedule[11][0], schedule[15][0], schedule[19][0], "-", "-"])
schedule_table.add_row([schedule[20][1], "-", "-", "-", "-", "-", schedule[20][0], schedule[22][0]])
schedule_table.add_row([schedule[21][1], "-", "-", "-", "-", "-", schedule[21][0], schedule[23][0]])

# writing to the file
schedule_file.write(str(schedule_table))

schedule_file.close()