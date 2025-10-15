#strings
s = "coffee"
t = "bread"
print(s)
print(t)
print(s+t) #concatinate the strings

#what happens if we say s[0]? or somethign similar
print(s[0])
#what if we put s[1:3]  (it starts form number 1 and stops before last number (stops before 3) thus stops on 2)
print(s[1:5])
#this is called string slicing
#we can't subtract strings print(s-t) = ERROR
s1 = '0123456789'
a =s1[0] #a = 0
b =s1[1] #b = 1
print(a)
print(b)
print(b+a) #what's output? 1 or 10? is are a , b strings or ints??
print(type(a))
print(type(b)) #conclusion, a,b are strings thus b+a is concatntion and thus 10
#now if we specifyi that a =intxyz and b = intabc then we'd get 1
a = int(s1[0])
b = int(s1[1])
print(b+a)
print(type(a))
print(type(b))