#let's say we ahve a cupboard, and we want a movin cupboard
#it needs wheels, extra facilities; increased cost
'''
let's say we have a list 
good, we can add and remove elements form it
what if we want a tuple? ()
it can't be changed after creation
while lists can..
why would anyone want a tuple
mabey we need fixed data..
improt.strings

'''
l = [5,10,7,26,78]
l.append(100)
print(l)
l.remove(7)
print(l)

t = (2,7,18,64,101,108,65)
#tuples have like 2 comands, we cna't change anything
#but we can index it , it's an unchangable data type
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits) 
s = string.ascii_letters
print(s) #printed as string
s = set(s) #every character becomes it's own element in the list
print(s) #printed as set, no longer a string
s = string.ascii_letters
alpha = tuple(list(s))
print(alpha) #now this is fixed, also notice how the order can become wonky base don how we chose add operations, modifyi our inputs to the vars
#let's say we have a string x, we want to remove special symbols form it
x = "thisisabvad^869580/.4489aebaer,taco%&bel0is decent"
l = list(x)
print(l)
r=[]
for i in l:
    if i in alpha:
        r.append(i)
print(r) #the above code helped us filter out special symbols form a std. given tuple. 

l = list(range(10))
t = tuple(range(10)) #now i wonder what their sizes are
import sys
print(sys.getsizeof(l))
print(sys.getsizeof(t))
#the size of the tuple is smaller