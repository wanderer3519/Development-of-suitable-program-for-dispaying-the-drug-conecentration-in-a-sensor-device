import pandas as pd

'''
    All the codes used in this file can be found at the following webpage
    https://www.digitalocean.com/community/tutorials/pandas-read_excel-reading-excel-file-in-python
    
    Here, pandas, a popular python library is used to read inputs from an excel sheet.
    After reading the input, it also gets the data specified in the coloumns to a hashmap.

    As an exercise, I have calculated the averages of the data present in specific coloums of the sheet.
'''

df = 0 # random init to avoid errors
df = pd.read_excel('../Cities_Probability(1).xlsx') # reads the entire sheet (by default the first sheet)


''' prints the entire sheet '''
# print(df) 

''' prints the coloumns '''
# print(df.columns.ravel()) 

''' gets a list representation of the elements in the specified coloumn '''
# print(df['population'].tolist())

input_data = {}
avg_values = {}
for col_name in df.columns.ravel()[1:]:
    input_data[col_name] = df[col_name].tolist()
    
    # initializing each value in avg_values
    avg_values[col_name] = 0

numeric = list(input_data.keys())[1:]

for col_name in numeric:
    for i in input_data[col_name]:
        avg_values[col_name] += int(i)
    avg_values[col_name] = avg_values[col_name] / len(input_data[col_name])

print(avg_values.values())

''' calculating the average of each coloumn as an exercise '''



# print(input_data)
