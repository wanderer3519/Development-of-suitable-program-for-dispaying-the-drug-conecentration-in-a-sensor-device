import intake as intk
import correlation as cr


if __name__ == '__main__':
    sheet = '../Test_input.xlsx'

    map = intk.read_input(xlsheet = sheet)
    currents = map['Current(mA)']
    times = map['Time(s)']

    time = times[3]
    current = intk.current(sheet, time)

    conc = cr.conc(current)
    print('The required conc is given by %.2f units' % (conc))
