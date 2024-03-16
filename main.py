import intake as intk
import correlation as cr


if __name__ == '__main__':
    
    # added a custom test input
    sheet = './Test_input.xlsx'

    # reading input into program
    map = intk.read_input(xlsheet = sheet)
    currents = map['Current(mA)']
    times = map['Time(s)']

    # giving a random time as input to get concentration
    inNum = int(input('Enter a random time index: '))
   
    # gets current for the given time input if valid
    try:
        time = times[inNum]

        current = intk.current(sheet, time)

    # gets the concentration for the desired time
        conc = cr.conc(current)

    # prints the result to output
        print('The required conc is given by %.5f M' % (conc))
    
    # if input is not valid, prints an error message
    except IndexError:
        print("Sorry, index is out of range. Please enter a valid index between 0 and %d." % (len(times) - 1))