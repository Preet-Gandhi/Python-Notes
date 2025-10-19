'''
think of a car and a bus
their differences
car -> high milage, low seats, mobile
bus -> low milage, high seats, imobile
we observe a trade off, each has it's own pros and cons
similar thing is present in python
'''
l =list(range(10))
print(l) #list form 0 to 9  
l.append("Preet")
l.append("India")
l.append(2.89477)
print(l)
#now we can scan L for certain elements
#ie. 
print(5 in l) #this shows that it can check the sublists and etc holding more values
print(-5 in l) #obv not as it's not in any related lists
#this is case sensitive
print(2.894770 in l) #true as 2.89477 is same as 2.894770
#if we make a lsit of a billion digits ie l = list(range(10000000000)) <overwrites l and makes it 0 to 999999999
#then we can call it's values at will 
#print(:[len(l)-1] in l)? would say yes and give max value 
#now it searches the wohole list all 1 billion inputs
#there has to be a faster way
del l
#what if we used curvy brackets instead of [], well we'd have a set then 
#sets don't have repeated elements 
y = {1,2,3,5,7,8,9,6,2,3}
print(type(y),y)
#remvoes repeated elements, lets us check what's inside (similar banner to lists) 
#l = list(range(billion)) #billion long list
x = set(range(10)) #set of a billion digits long 
s = set(range(10))
print(s,x)
#s = set(range(billion)) 
print("complete")
#the generation of the set took even longer than the list of same enteries
#if we search for 0 in l we'd get true as l has everything fomr 0 - 999 999 999
#if we say -1 or somethign else in l, it'll take a v.long time to give us the anser , as it checks every one of the billion entries
#what if we test -1 in s the set (still 1 billion big) the anser is isntant, false
#how are sets returing fast outcomes?
#how does it determine belongingness
#here we had a trade off
'''
list -> lsit searching difficult , 
set -> set searching is easy , 

'''
import random
import math
import sys 
l = []
l1 = [0]
l2 = [0,1]
print(sys.getsizeof(l))
print(sys.getsizeof(l1))
print(sys.getsizeof(l2)) #gives how much space each set has in bytes , we see howw it's size increases
x = list(range(100))
s = set(range(100))
print(sys.getsizeof(x))
print(sys.getsizeof(s))
# wtf, list size is 856, set size is... 8408 bytes... 
#thus list -> smaller size, harder to find beloning
#sets -> easier to find belonging, larger size
#perhaps a list is car and set is bus, set has some ability lists can do while sets can't
#print(s[0])  s[0] is giving error while other inputs also are, s1 , s2, 3 , 4 ...
#while lists let us easially acess the elements 
#set is not subscriptable (we cna't call it's elements, there is no 3rd elements, we can only tell
#if an aelement is present o rnot, it has no idea waht element 3 is
#so mabey sets have no preserved order but rather preserved numberical contents
del l,y,x,s,l1,l2
z = {"Preet","Preeti","Pratyush","Prateek","Mohandas karamchandra gandhi"}
#we can also add to z
z.add("Himank Jain")
#z[0] doesn't exist, also inotedied when we print z it has ranodm config on ppls devices
#sometimes added value is in fornt, or backwards, or in middle 
#basicly every thing has it's own abilities, we'll be taught mroe in DSA
