i = 10
f = 9.8
s = "abc"
l = [1,2,"abc",9.7,[1,2,3],False]
b1 = True
b2 = False
print(type(b1))
print(type(b2))
#we have a new data type boolean. It can only have 2 values. True or False
# the T and F has to be capital
# Data conversion
a=int(1.5)
c=int('10')
#we're asking computer to turn 1.5 into int, '10' into int-print(type(a),a)
print(type(a),a)
print(type(c),c)
#notice how when 1.5 gets converted into an int. It drops the decimal part. 
#it only takes whole number part. no diget rounding 
b=float(10)
d=float('9.8')
g=float('10')
#e=float('abc') this results in error
#we're trying to convert an int into a float and a string into a float
print(type(b),b)
print(type(d),d)
#print(type(e),e) this can't be printed as e can't be defined
print(type(g),g)
#it just ads a .0 after the wohole number of the int
#it takes out the numbers form inside the string, if it's a float then no change
#if it's not a float then it ads .0 at the end

h=str(10)
j=str(9.8)
#now what if we want to convert int and float into str
k=str(True) #it'll just print the true or false (turns everything it can into text)
print(type(h),h)
print(type(j),j)
print(type(k),k)
#we've been converting between datay types this is refered to as
#type conversion or type casting
#what about casting w.r.t boolean
m=bool(10)
n=bool(0)
o=bool(-10)
print(type(m),m)
print(type(n),n)
print(type(o),o)
#only bool 0 is false rest is +ve
#what about float and string to bool?
p=bool(9.8)
q=bool(0.0)
r=bool(-9.8)
print(type(p),p)
print(type(q),q)
print(type(r),r)
#same result again 0.0 wich is 0 is false, rest is true
#what about string to bool?
s1=bool("abc")
s2=bool("")
s3=bool(" ")
s4=bool("0")
print(type(s1),s1)
print(type(s2),s2)
print(type(s3),s3)
print(type(s4),s4)
#empty strings are false, rest true
#s4 still has a value in it's sring. the value bing character 0, not number. thus it's true
#bool representation of 0 is always false
#bool rep of string is always true except empty string