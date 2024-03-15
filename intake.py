import pandas as pd

'''
    All the codes used in this file can be found at the following webpage
    https://www.digitalocean.com/community/tutorials/pandas-read_excel-reading-excel-file-in-python
    
    Here, pandas, a popular python library is used to read inputs from an excel sheet.
    After reading the input, it also gets the data specified in the coloumns to a hashmap.

    As an exercise, I have calculated the averages of the data present in specific coloums of the sheet.
'''

df = 0 # random init to avoid errors
df = pd.read_excel('../Test_input.xlsx') # reads the entire sheet (by default the first sheet)


''' prints the entire sheet '''
# print(df) 

''' prints the coloumns '''
# print(df.columns.ravel()) 

''' gets a list representation of the elements in the specified coloumn '''
# print(df['population'].tolist())

input_data = {}

for col_name in df.columns.ravel():
    input_data[col_name] = df[col_name].tolist()

print(input_data)

''' calculating the average of each coloumn as an exercise '''



# print(input_data)
