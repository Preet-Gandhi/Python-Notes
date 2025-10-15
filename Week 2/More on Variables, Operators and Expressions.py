'''
we've seen and or or some other keywords, these are special words. they're reserved
/consided part of progrmaing langage
we cna't use them as var names
i.e
and = 5 is phorobited -> error
'''
abc_w489 = "taco" #only alphonumeric and _ can be in as var names
del abc_w489
#numbers 8902, can't start a var name
# 3globe = 5 will be an error
''' var naems are case sensitive'''
roll = 5
r0ll = 68
Roll = 6
ROLL = 7
print(roll,r0ll,Roll,ROLL) #they all are different
del roll,r0ll,Roll,ROLL
#multi assignment, we can declare and assign multiple variables of differnt types in one statement/line
x,y,z = True,35.78,"hello"
print(x,y,z)
#there must be as many definitions as variabels or there'll be an error
#we can also say
x=y=z=687
print(x,y,z)
#all have same value
#now we can also go. 
x,y = 10,20
print(x,y)
x,y = y,x
print(x,y)
#variable switching. 
#How to remove variable? we cna't have hundreds or thousands of them.
x = 10
print(x)
del x,y,z # this will delete x
#print(x) error as x does not exist. 
''' short hand operators
arethmetic operators
let's say we count'''
count = 0
count = count +1 #idealy we'd type this but we could type
print(count)
count +=1
count +=1
print(count)
del count
#this can also be -=, *=, /=, //=, %=, &-, ^=, <<= , >>= , etc. 
#in operator -> search engine operator, lets us check if operand a is in operand b
name1= " james bond hueston von ivankavish"
name2 = " james bond" 
print(name2 in name1)
print(name1 in name2)
print("taco"in "taco are divine food form the fifthentheournat circut of taco land")
#result of in is always boolean value
#operator chaining 
'''
x = 5
print(1< x < 10)
print(10 < x < 20)
print(x < 10 < x*10 < 100)
print(10 > x <= 9)
print(5 == x > 4) <5 is equal to x, x>4> this is once agian only outputed as true /false
each of them ahs multiple operators in one statement. what's their execution?
'''
print("here's the part about operator chaining")
x = 5
print(1< x < 10)
print(10 < x < 20)
print(x < 10 < x*10 < 100)
print(10 > x <= 9)
print(5 == x > 4)
del x,name1,name2
