'''#how to import a library in different ways?
import calendar
print(calendar.month(2025, 10))
#what if i want to print calander of an year?
print(calendar.calendar(2025))
'''
'''
from calendar import *
print(calendar(2025)) #this also has same output as above print(calendar.calendar(2025)) but we didn't write import calander... hmm?
#earlier we wrote import calander, it improts entire libear and we'd only be able to acess anything inside with the keyword caalander
#but putting form calander import * imports everything from calander into our program, no need to write calander.(xyz)
print(month(2025, 10)) #this also has same output as above print(calendar.month(2025, 10)) but we didn't write calendar. before month
#now if from calandar import* was commented out and we had import calandar it wouldn't work
'''
'''
#it's unesseary to import everythign and use one feature... what if
from calendar import month
print(month(2025, 10))#this exclusivly imports month from calander but other functions of calandar won't work
print(month(2026,12)) #most ideal way to write program if a few featurs are being used
'''
#now we can import the entire library and store it in variable
import calendar as c
print(c.month(2025, 12))
#or
from calendar import month as m
print(m(2027,12))
del c,m