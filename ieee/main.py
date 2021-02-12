import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import json
#source ./env/bin/activate # command line past to activate virtual environment
#change directory: cd /Users/thomasnguyen/Desktop/Programming/Python/ieee

print("Reading Excel file...")
print("Year: 2017-2018...")
print('\n')
pd.set_option('display.max_rows',None,'display.max_columns',None) # display rows and columns up to a limit of 'None' (no limit)
df = pd.read_excel('IEEE_Member_App_17-18.xlsx', sheet_name='Membership',usecols=['Last Name', 'First Name','Major (for statistical purposes only)', 'Classification (for statistical purposes only)','Total points'],nrows=235) # read excel file into dataframe variable 'df'

# Print name of columns that are loaded in
cols = list(df.columns) # convert the columns into a list
print("The available columns are:")
print(*cols, sep=', ') # *cols is direct addressing which removes the syntax of a list
print('\n')

# Determine membership classification composition & number of points 
class_list = df['Classification (for statistical purposes only)'].to_list() # converts membership classification column into a list
points_list = df['Total points'].to_list() # converts total points column into a list
fm = 0
sm = 0
jn = 0
sr = 0
gd = 0
nl = 0
fm_tp = 0.0
sm_tp = 0.0
jn_tp = 0.0
sr_tp = 0.0
gd_tp = 0.0
nl_tp = 0.0
class_list_total = 0

# Error encountered (resolved):
# print(points_list,"\n") # What is in the element of the list of an empty excel cell? Answer: 'nan'
# print(type(points_list[3])) # What type of variable is 'nan'? Answer: float --> must convert element to string to use ==
for i in range(len(points_list)):
    if str(points_list[i]) == 'nan':
        points_list[i] = 0.0

for i in range(len(class_list)):
    if class_list[i] == 'Freshman':
        fm = fm + 1
        fm_tp = fm_tp + points_list[i]
    if class_list[i] == 'Sophomore':
        sm = sm + 1
        sm_tp = sm_tp + points_list[i]
    if class_list[i] == 'Junior':
        jn = jn + 1
        jn_tp = jn_tp + points_list[i]
    if class_list[i] == 'Senior':
        sr = sr + 1
        sr_tp = sr_tp + points_list[i]
    if class_list[i] == 'Graduate':
        gd = gd + 1
        gd_tp = gd_tp + points_list[i]
    if str(class_list[i]) == 'nan':
        nl = nl + 1
        nl_tp = nl_tp + points_list[i]

print("Number of freshmen:",fm)
print("Number of sophomores:",sm)
print("Number of juniors:",jn)
print("Number of seniors:",sr)
print("Number of graduates:",gd)
print("TOTAL NUMBER OF MEMBERS:",(fm+sm+jn+sr+gd))
print('\n')

print("Total points for freshmen:",fm_tp)
print("Total points for sophmores:",sm_tp)
print("Total points for juniors:",jn_tp)
print("Total points for seniors:",sr_tp)
print("Total points for graduates:",gd_tp)
max_p = max(fm_tp, sm_tp, jn_tp, sr_tp, gd_tp)
most_active_class = ''
if max_p == fm_tp:
    most_active_class = 'FRESHMEN'
if max_p == sm_tp:
    most_active_class = 'SOPHOMORES'
if max_p == jn_tp:
    most_active_class = 'JUNIORS'
if max_p == sr_tp:
    most_active_class = 'SENIORS'
if max_p == gd_tp:
    most_active_class = 'GRADUATES'
if max_p == nl_tp:
    most_active_class = 'NOT LISTED'
print("MOST ACTIVE CLASS:",most_active_class)
print('\n')

# Determine membership major composition
# https://www.geeksforgeeks.org/python-add-the-occurrence-of-each-number-as-sublists/
major_list = df['Major (for statistical purposes only)'].to_list() # convert column of majors to a list
for i in range(len(major_list)):
    if str(major_list[i]) == 'nan':
        major_list[i] = 'Not listed'
l = [] # sub lists
unq_l = [] # master list
def count_occur(list1): # create function called "count_occur"
    for i in range(0, len(list1)): 
        a = 0
        row = [] # create empty list
        if i not in l: # 'l' is empty, so this statement should loop everytime 'for i in range(0, len(major_list))' is entered
            for j in range(0, len(list1)): 
  
                # matching items from both lists 
                if list1[i] == list1[j]: 
  
                    # on match counter increments by 1 
                    a = a + 1
  
            row.append(list1[i]) 
            row.append(a) 
  
            # append function will append 1ist1 list items to 2d list
            l.append(row) 
              
    # below code is to eliminate repetitive list items     
    for j in l: 
        if j not in unq_l: 
            unq_l.append(j) 
              
    return unq_l
    
count_occur(major_list) # prints list of lists that has Major type and Number of Major type
unq_major_list = [] # must be created to be used in dynamic graph as different axis
for i in range(0,len(unq_l)):
    for j in range(0,1):
        print("Number of",unq_l[i][j],"Majors:",unq_l[i][j+1])
        unq_major_list.append(unq_l[i][0]) # only want the Major type
print("\n")
# print(unq_major_list,"\n") # prints list of all member's majors

# Stats plan: 
# Which major has the most points?
# Which classification has the most points?
# Create graph for general meetings (x: classification, y: major, z: # of attended meetings)
# Create graph for event (x: classification, y: major, z: # of attended events)
# Create graph for all event (x: classification, y: major, z: # of all attended events)

# 3D Graphing
# Convert class_list to plottable data, assign class type to a number
plt_class_list = []
for i in range(len(class_list)):
    if class_list[i] == 'Freshman':
        plt_class_list.append(1)
    if class_list[i] == 'Sophomore':
        plt_class_list.append(2)
    if class_list[i] == 'Junior':
        plt_class_list.append(3)
    if class_list[i] == 'Senior':
        plt_class_list.append(4)
    if class_list[i] == 'Graduate':
        plt_class_list.append(5)
    if str(class_list[i]) == 'nan':
        plt_class_list.append(6)

# Convert major_list to plottable data, assign major type to a number 
plt_major_list = []
for i in range(len(major_list)):
    for j in range(len(unq_major_list)):
        if major_list[i] == unq_major_list[j]:
            plt_major_list.append(j+1)

fig = plt.figure(figsize = (12,9)) # specify figure size
ax = plt.axes(projection ="3d")
ax.scatter3D(plt_class_list, plt_major_list, points_list, s=100, c='green') # specify marker size and color, plot (x,y,z)
ax.set_title('Membership Activity Classification', size=12)
plt.xticks(fontsize=8, rotation=0)
plt.yticks(fontsize=6, rotation=0)
# ax.set_xticks(range(6)) # sets the boundaries of xticks                     LIBRARY ERROR CAUSES CUT OFF 
# ax.set_xticklabels(['Freshman','Sophomore','Junior','Senior','Graduate','Not listed'])
ax.set_yticks(range(len(unq_major_list))) # ensure that all tick marks are shown, make # of tick marks = # of unique majors
# unq_major_list = json.dumps(unq_major_list) # adds double quotes around every element in the list
ax.set_yticklabels(unq_major_list) # assign all unique majors to ytick labels 
ax.set_xlabel('Classification (x)', size=10)
ax.xaxis.labelpad = 20 # changes spacing of xlabel relative to axis
ax.set_ylabel('Majors (y)', size=10)
ax.yaxis.labelpad = 30 # changes spacing of ylabel relative to axis
ax.set_zlabel('Total Points (z)', size=10)
plt.show()
