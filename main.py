import intake as intk
import correlation as cr


if __name__ == '__main__':
    
    # added a custom test input
    sheet = '../Test_input.xlsx'

    # reading input into program
    map = intk.read_input(xlsheet = sheet)
    currents = map['Current(mA)']
    times = map['Time(s)']

    # giving a random time as input to get concentration
    time = times[3]

    # gets current for the given time input
    current = intk.current(sheet, time)

    # gets the concentration for the desired time
    conc = cr.conc(current)

    # prints the result to output
    print('The required conc is given by %.2f units' % (conc))
