print("Type your name:")
n=str(input())
print("Type your location:")
l=str(input())
print("Hello",n,"how's the weather in",l,"?")
print("Type your age:")
a=int(input())
print("Good to know that you are",a,"years old.")
#can we combine taking input and printing?
c=str(input("Type your name: "))
b=str(input("Type your location: "))
d=int(input("Type your age: "))
print("Hello",c,"how's the weather in",b,"? Good to know that you are",d,"years old.")
#can we change the values of age,name and location or are they fixed?
#yes it chagnes, it's value varriates. c,b,d,n,l,a are variables
#variables are containers that store data nothing else
#they can store different values and be updated/change later on
#but the values they sotre "Preet", "40" are literals. They're actual values
#values can be modified when needed
age = 25
age = age + 1 #is valid but.
#30=30+1 is invalid
#because 30 is a literal and literals cannot be changed
#literals can only be used on rhs of an assignment
#variables can be used on both lhs and rhs of an assignment
r=int(input("Gime a radius"))
pi=3.14
area = r*r*pi
print("Area of circle is",area)
#vars are only used when value can change,else we use literals
