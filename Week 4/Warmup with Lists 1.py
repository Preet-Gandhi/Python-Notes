#we know what lists are
L1 = [ 1,7,4,"feoear",True,type(['a','b','c']), ['a','b','c']]
print(L1)
#append adds to end of list, list can include the same item more than once
L1.append(7)
print(L1)
#this is not a set
#we also have other methods like .remove()
L1.remove(1)
print(L1)
del(L1)
#.remove(x) removes the first occurance of x in the list (reads form left to right), (top to down) 
#Matrix in python
L1 = []
L1.append(1)
L1.append(2)
L1.append(3)
print(L1) #we created an L1 and assign it values
x = [] #we create an array x and append L1 to it
x.append(L1)
print(x)
# first element of array x is the array L1 itself
m = []
m.append(4)
m.append(40.75)
m.append("4")
print(m)
x.append(m)
print(x) #now x is an array with multiple arrays inside 
t=[]
t.append(x)
print(t) #a list in a list in a list 
t.append([100,101,1000])
print(t)
# t = [ element 1 [E1L1[1, 2, 3], E1L2[4, 40.75, '4']], element 2 [100, 101, 1000]] element 1 is a list in the list, e2 is a list in the list
#thus t[0] should be e1
print(t[0])
del t,m,x,L1
#now let's create a matrix
m = []
m.append([1,2,3])
m.append([4,5,6])
m.append([7,8,9])
#now this adds the lists as the respective element sof m
print(m)
#now we can acess elements on m
print(m[0], m[0][0]) #prints list 0 , prints first element of list 0 
#kinda like m[i][j], or m[i][j][k] or etc... 
#this is a 2D data (matrix)
