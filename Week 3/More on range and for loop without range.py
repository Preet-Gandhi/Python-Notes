#what if we want to print all the odd numbers form 1 to 10? with no if conditoin?
for i in range(1,11,2): #the 3rd paramater is called step and lets us add properties (step, how mcuh it increases by)
    print(i)
#even if we provide one or 2 paramters, it always takes defualt values -> start is 0, step is 1
#range has 3 paramaters -> start - defualt 0, end - no default, step - default one
#what if I want to print number sbackwards
for i in range(10,0,-1):
    print(i) #here we took start point form 10 end point will be 1 and step is -2 ... it dereases
#rangeless for loop?; for each loop
country = "India"
for letter in country:
    print(letter)
#this goes through the string ch by chna nd prints it, I n d i a 