# source ./env/bin/activate # command line past to activate virtual environment
# change directory: cd /Users/thomasnguyen/Desktop/Programming/Python/ieee

import pandas as pd

print("Reading Excel file...")
print("Year: 2017-2018...")
print('\n')
pd.set_option('display.max_rows',None,'display.max_columns',None) # display rows and columns up to a limit of 'None' (no limit)
df = pd.read_excel('IEEE_Member_App_17-18.xlsx', sheet_name='Membership',usecols=['Last Name', 'First Name','Major (for statistical purposes only)', 'Classification (for statistical purposes only)','Total points'],nrows=90) # read excel file into dataframe variable 'df'

# Print name of columns that are loaded in
cols = list(df.columns) # convert the columns into a list
print("The available columns are:")
print(*cols, sep=', ') # *cols is direct addressing which removes the syntax of a list
print('\n')

# Determine membership classification composition
class_list = df['Classification (for statistical purposes only)'].to_list() # converts column into a list
fm = 0
sm = 0
jn = 0
sr = 0
gd = 0
class_list_total = 0
for i in range(len(class_list)):
    if class_list[i] == 'Freshman':
        fm = fm + 1
    if class_list[i] == 'Sophomore':
        sm = sm + 1
    if class_list[i] == 'Junior':
        jn = jn + 1
    if class_list[i] == 'Senior':
        sr = sr + 1
    if class_list[i] == 'Graduate':
        gd = gd + 1

print("Number of freshmen:",fm)
print("Number of sophomores:",sm)
print("Number of juniors:",jn)
print("Number of seniors:",sr)
print("Number of graduates:",gd)
print("Total number of members:",(fm+sm+jn+sr+gd))
print('\n')

# Determine membership major composition
# https://www.geeksforgeeks.org/python-add-the-occurrence-of-each-number-as-sublists/
l1 = df['Major (for statistical purposes only)'].to_list() # convert column of majors to a list
l = [] # sub lists
unq_l = [] # master list
def count_occur(list1): # create function called "count_occur"
    for i in range(0, len(list1)): 
        a = 0
        row = [] # create empty list
        if i not in l: # 'l' is empty, so this statement should loop everytime 'for i in range(0, len(l1))' is entered
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
    
count_occur(l1) # prints list of lists that has Major type and Number of Major type
for i in range(0,len(unq_l)):
    for j in range(0,1):
        print("Number of",unq_l[i][j],"Majors:",unq_l[i][j+1])
print("\n")

# Stats plan: 
# Which major has the most points?
# Which classification has the most points?
# Create graph for general meetings (x: classification, y: major, z: # of attended meetings)
# Create graph for event (x: classification, y: major, z: # of attended events)
# Create graph for all event (x: classification, y: major, z: # of all attended events)
