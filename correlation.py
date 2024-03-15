'''
    This file contains the correlation between current and concentartion.
    
    The correlation between current passed through an electrolyte and concentration of the electrolyte
    is given by the least square fit / linear regression relation.

    It is of the form 
    y = m * x + c
    where 
        m is the SLOPE of the graph
        c is the y INTERCEPT of the graph

    This equation is calculated by taking certain (x,y) values and performing linear regression on them.
'''

SLOPE = 1.385
INTERCEPT = 0.0234

def current(conc: int) -> int:
    y = SLOPE * conc + INTERCEPT
    return y

def conc(current: int) -> int:
    x = (current - INTERCEPT) / SLOPE
    return x

'''
    From the spreadsheet current value is known to us at a given time.
    We have to find the concentration value then.
    So we have to find concentation for a given current.

    Since our plot is current vs concentration plot (y vs x),
    We need to obtain x for a given y
    The above helper functions are there to do it for us.

    We only need to obtain input current from the spreadsheet.
'''
