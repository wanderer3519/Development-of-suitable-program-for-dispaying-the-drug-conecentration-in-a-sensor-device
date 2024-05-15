import pandas as pd
from flask import Flask
from scipy.stats import linregress

app = Flask(__name__)

''' 
    Here, pandas, a popular python library is used to read inputs from an excel sheet.
    After reading the input, it also gets the data specified in the coloumns to a hashmap.

    As an exercise, I have calculated the averages of the data present in specific coloums of the sheet.
'''
xlsheet = './Test_input.xlsx'

def read_input(xlsheet: str):
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
    
    temp: dict[str, list] = read_input(xlsheet)
    time_list: list[int] = temp['Time(s)']
    current_list: list[float] = temp['Current(mA)']

    ''' One type of implementation '''
    '''
        index: int = time_list.index(time)  
        retval: float = current_list[index]
    '''

    ''' Or else, map each of the values in "Time(s)" to "Current(mA)" '''
    
    hashMap: dict[int, float] = {time_list[i] : current_list[i] for i in range(len(time_list))}
    retval: float = hashMap[time]

    return retval


def avg_current(xlsheet: str, voltage) -> float:
    i = 0
    data = read_input(xlsheet=xlsheet)
    currents = data['Current(mA)']
    voltages = data['Voltage(V)']

    sum_curr = 0
    len_curr = 0
    i = voltages.index(voltage)

    while(voltages[i] == voltage):
        sum_curr += currents[i]
        len_curr += 1
        i += 1

    avg_curr = sum_curr / len_curr
    avg_curr = round(avg_curr, 3)
    return avg_curr

# sheet = './Test_input.xlsx'
# avg_curr = avg_current(sheet)
# print(avg_curr)


'''
    Here, we move on to calibration. We are given another xlsx of calibration and we are asked to get slope and intercept.
    Here, we use scipy to calculate this. 'linregress' function from scipy is used to perform linear regression on the data
    We in turn, get back the slope and y-intercpt as follows

    y = ax + b
    Where a is the slope and b is the intercept. 
    These two are calculated by linregress function
    
    Let sum() denote the summation of all values of that input
    Let n be number of data items
    
    a = (sum(y) * sum(x ** 2) - sum(x) * sum(x * y)) / (sum(x ** 2) - (sum(x)) ** 2)
    b = (n * sum(x * y) - sum(x) * sum(y)) / (n * sum(x ** 2) - (sum(x)) ** 2) 
'''
def calculate_slope_and_intercept(xlsheet: str, x_column: str, y_column: str) -> tuple:

    data = read_input(xlsheet)

    x_values = data[x_column]
    y_values = data[y_column]

    slope, intercept, r_value, p_value, std_err = linregress(x_values, y_values)

    return slope, intercept
    
'''
    After knowing slope and intercept, it is very easy to calculate the concentration. We just map the average current to concentration on the graph

    current = slope * concentration + y-intercept
    concentration = (current - y-intercept) / slope 
'''
def calculate_concentration(xlsheet: str, x_column: str, y_column: str) -> tuple:

    data = read_input(xlsheet)
    # curr = data['current']

    x_values = data[x_column]
    y_values = data[y_column]

    slope, intercept, r_value, p_value, std_err = linregress(x_values, y_values)

    curr = avg_current('./Book1.xlsx', 'conc')

    conc = (curr - intercept) / slope
    return conc

# print(read_input(xlsheet))
inputData = read_input(xlsheet)
avgCurr = avg_current(xlsheet, 66)
# print(avgCurr)