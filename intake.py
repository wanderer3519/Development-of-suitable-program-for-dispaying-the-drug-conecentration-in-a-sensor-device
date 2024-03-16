import pandas as pd

'''
    All the codes used in this file can be found at the following webpage
    https://www.digitalocean.com/community/tutorials/pandas-read_excel-reading-excel-file-in-python
    
    Here, pandas, a popular python library is used to read inputs from an excel sheet.
    After reading the input, it also gets the data specified in the coloumns to a hashmap.

    As an exercise, I have calculated the averages of the data present in specific coloums of the sheet.
'''
# xlsheet = './Test_input.xlsx'

def read_input(xlsheet: str) -> dict[str, list]:
    df = 0 # random init to avoid errors
    df = pd.read_excel(xlsheet) # reads the entire sheet (by default the first sheet)

    ''' prints the entire sheet '''
    # print(df) 

    ''' prints the coloumns '''
    # print(df.columns.ravel()) 

    ''' gets a list representation of the elements in the specified coloumn '''
    # print(df['population'].tolist())

    input_data: dict[str, list] = {}

    # converting xlsheet into a hashmap
    for col_name in df.columns.ravel():
        input_data[col_name] = df[col_name].tolist()

    return input_data


'''
    Get a value of current for a given time input.
    This one has two styles of implementation.
    Any one of the styles discussed below will do fine.
'''
def current(xlsheet: str, time: int) -> float:
    ''' One type of implementation '''
    
    temp: dict[str, list] = read_input(xlsheet)
    time_list: list[int] = temp['Time(s)']
    current_list: list[float] = temp['Current(mA)']

    index: int = time_list.index(time)  
    retval: float = current_list[index]

    ''' Or else, map each of the values in "Current(mA)" to "Time(s)" '''
    
    hashMap: dict[int, float] = {time_list[i] : current_list[i] for i in range(len(time_list))}
    retval: float = hashMap[time]

    return retval
