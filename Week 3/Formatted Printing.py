#what're the other featurs of print statements?
#every time the computer goes across a print statement, it's printed on a new line
#what if we want to stay in same line -> use end paramater, end = " "
for x in range(10):
    print(x, end = " ") #instead of 1, 2, 3, 4, 5, 6, 7, 8, 9 we get 1 2 3 4 5 6 7 8 9 
#default end paramater of print ix \n 
#let's try to print todays date
d = 15
m = 12
year = 2025
print("Todays date is",d,m,year) #we always put hiphen/slash in between, well why is space 
#being added between 15 12 2025 
#that's due to seperator value, default seperator value is " ", but we can specify it to be anythign we want
print("Todays date is ", d,m,year, sep = "-")#see how ther's line infront of 15, ugly
print("Todays date is", end=" ")
print(d,m,year, sep = "/")
#let's say we want to print a multiplication statement with a for loop
num = int(input())
for i in range(1,11):
    print(num,"*",i,"=",num*i)
#isntead we could type; we have f" or f' print (formated print), entire statement is written as one string
for i in range(1,11):
    print(f"{num} X {i} = {num*i}") #or it fould have been f' instead of f", only those thing in {} are var, rest strings
#enother way 
for i in range(1,11):
    print('{0} X {1} = {2}'.format(num,i,num*i)) #here what ever is in {} is replaced with it's ref. var
#this is pritning using format function 
#python also allows prining using moudlio operators
print("%d X %d = %d" % (num,i,num*i))
#f' and f" is more useful than regular print functions
pi = 22/7
print(f'The value of pi = {pi}')
print("The value of pi = {0}".format(pi))
print("The value of pi = %f" % pi) #very old way of writing strings, has limitations
#how to tell comp i want only 2 digits instead of long value of pi? -> format specifiers
print(f'The value of pi = {pi:.2f}')
print("The value of pi = {0:.2f}".format(pi))
print("The value of pi = %.2f" % pi) #we're explicity telling the computer we want 2 decimal poitns after the . (decimal point)
print("{0}".format(1))
print("{0}".format(11))
print("{0}".format(111))
print("{0}".format(1111))
print("{0}".format(11111)) #notice how it forms a triangle
#we can make the pattern align it self to look good -> right indentation
print("{0:5d}".format(1)) #our max length is 5 characters so we show{0:5d} the 5d indicates we want to
print("{0:5d}".format(11)) #use min 5 characters so it adds blanks
print("{0:5d}".format(111))
print("{0:5d}".format(1111))
print("{0:5d}".format(11111))
#pattern is now right alligned, rather than left