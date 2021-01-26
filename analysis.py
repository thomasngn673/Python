# source ./venv/bin/activate # command line past to activate virtual environment + change directory
import pandas as pd

# Read csv file
print('Read csv file')
df = pd.read_csv('pokemon_data.csv') # dataframe
print(df.head(3))
print('\n')

# Read excel file
print('Read excel file')
df_xlsx = pd.read_excel('pokemon_data.xlsx')
print(df_xlsx.head(3))
print('\n')

# Read txt file
print('Read txt file')
df = pd.read_csv('pokemon_data.txt', delimiter='\t') # if delimiter is not added '\t' is explicitly printed in output
print(df.head(3))
print('\n')

# Read column names
print('Read column names')
print(df.columns) # outputs the name of each column
print('\n')

# Print specific columns
print('Print specific columns')
df.columns
print(df['Name']) # print all pokemon names
print('\n')
print(df['Name'][0:5]) # print first 5 names
print('\n')
print(df[['Name','Type 1', 'HP']])
print('\n')

# Print specfic rows
print('Print specfic rows')
print(df.iloc[1]) # print integer location 1 (first row)
print('\n')
print(df.iloc[1:4]) # print first 4 rows
print('\n')

# Print specific location
print('Print specific location')
print(df.iloc[2,1]) # print [Row, Column]
print('\n')

# Print each row
print('Print each row')
for index, row in df.iterrows(): # iterate through rows and print index number & name
    print(index, row['Name']) # print all index # and names
print('\n')

print(df.loc[df['Type 1'] == "Fire"]) # find all row #'s where Type 1 == fire --> pass into func that prints values (row) at locations
print('\n')

# Desribing Data
print('Describing Data')
print(df.describe()) # provides statistical analysis such as mean, min, max, stdev
print('\n')

# Sorting data alphabetically
print('Sorting data alphabetically')
print(df.sort_values('Name', ascending=False)) # sorts data by name in descending order (ascending by default)

# Making changes to data
print('Making changes to data 1')
# Add up all stats to determine which the strongest pokemon is
df['Total Points'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] # new column is added as last column to end by default
print(df.head(3))
print('\n')

# Removing changes in data
print('Removing changes in data')
df = df.drop(columns=['Total Points']) # drop column that is named 'Total Points'
print(df.head(3))
print('\n')

print('Making changest to data 2')
df['Total Points'] = (df.iloc[:, 4:10]).sum(axis=1) # df.iloc[rows, columns] lists all values specified; .sum(axis=1) adds horizontal rows, .sum(axis=0) adds vertical rows