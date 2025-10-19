#we have a set up 2 lits and then we try to prefor operations on them, what will happen?
L1 = [1, 2, 3]
L2 = [10, 20, 30]
print(L1, L2)
#what if we ad L1 and l2?
L1l2 = L1 + L2 
L2l1 = L2 + L1 
#let's print
print(L1l2,"L1 + L2", L2l1, "L2 + L1" )
#upon seeing output we notice it appends the lists/arrays 
#the elements of l2 are added to l1 (After the elements of l1) and vise versa for L2 + L1
#it should be called concatination of lists (L2 is appened to L1)
print("Notice how the lists above printed as [a,b,v,c, ...], yeah that was the print operator")
print(L1)
del L1,L2,L1l2,L2l1
#for matrices we want the start values to be 0. it's tedious to type [0,0,0,0,0,... n times]
n=int(input('give order of square matrix'))
M = [0]*n 
print(M) 
#[0]*n just menas making an aray with n elements of the value inside of the [] (square brackets)
#this is possible with multiple elements not just 0
m = [1,2,3,4]*n
print(m)
#equality?
l1 = [1,2,3]
l2 = [1,2,3]
l3 = [1,3,2]
print(l1 == l2)
print(l1 == l3) #for comparision lists need to have exact same elements in the same indexing 
#it's possible to compare, the lists compares element vise
print(l2 < l3, l3 < l2) #first is true and 2nd is false
#it comapres elements if one list has more elements then it'd compare aginst nothign to something
#then somehting would always be greater
#you must remember how we can update the indexing in python
l=[1,2,4]
print(l)
l[2]=3
print(l)
#notice hwo value of l is updated, as it can do that it's called mutable
#try doing what with a string
a = "preet"
print(a)
#a[2]="o" error, string done't support item assignment, we can't reasign the indexing values of a stirng
l1 = [1,2,3]
l2=l1
l1[0]=100
print(l2,l1)
#supprised? why are they the same?
#with lists the beheaviour is different, due to internal implimentation of lists in python
'''
we say x = 5, y = x , y = 10 here the computer stores location for x and assigns value, then
it stors location for y and stores x's value then it finds y and updates it's value,
but for a list 
computer allots memory block to l1. It's names and values are stored in it
when we say l2 = l1; computer adds another name to the memory location, location is same jsut
different ways to call it
'''
#creat seprate copy of l2
l2=list([l1])
l3=l1[:]
l4 = l1.copy()
l5=l4
#then any changes in l2,l3,l4, are specific to them only
#is operator checks if the lists are pointing to same location
print(l1 is l2, l1 is l3, l1 is l4, l1 is l5)
#if false then they have different memory locations 
#now what if it's pased as argument to function
def add(x):
    x=x+1
    return x

x=5
print(add(x)) #here we take gloabla value into local var and then give output withouth updating global value
print(x) #notice hwo x's values are differnt here it's global var
#what about lists? 
def add(x): #here we're not passing value of x, we are passing the list x it self
    x.append(1) #thus this updates the orignal list value 
    return x #returns orignal list (

x=[5]
print(add(x))
print(x) 
#notice hwo both outcomes are the same? [5,1]
#list methods
x = [1,2,3]
x.append(1) #adds element to list
x.remove(2) #removes element form list
z = x.copy()
print (x,z)
x.insert(2,9) #first paramater where/what index it'll be inserted as, second paramater is value
print(x)
x.pop(0) #computer deletes element at index 0
print(x)
x = [ 1,5,1,86,56,5,53567] #list needs to be sorted
x.sort() #sorts form decending to ascending
print(x)
x = [ 1,5,1,86,56,5,53567] #list needs to be sorted
x.reverse() #reverses orignal list order
print(x)
del x, l2, l3, l4, l5,l1,l,m,n,a 