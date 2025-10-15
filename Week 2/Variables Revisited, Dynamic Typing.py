a = 10
print(type(a)) #here it was only int
a = "India"
print(type(a)) #now it's turned into an str
#a computer stores different types of data in different places. if we say a = 10 
#it creates a memory location where a and it's value is cored
#but when u say a is india then it looses it's value a and becoems a string
#this is dynamic typing (noun type not typing on keyboard) (variable related), variables have flexiability
a = 10
print(type(a))#it becomes int
a = a/2 
print(type(a))#it becomes float .. thus division might convert ints into floats
