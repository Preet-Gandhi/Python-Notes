#lets say we have a scientific calculator.  oki so we firs tneed to import a math
import math,random #python has math libeary by defualt and it adds those functions to our code
#now we can use the functions in the math library withouth needing to define them ourselves
#slowly going and fetching the math funcitons form the libeary every time is tedious process
print(math.log(10))
print(math.sqrt(16))
print(math.factorial(4))
print(random.random()) #random.random gives a random number between 0 and 1
print(random.randint(1,100)) #gives a random integer between 1 and 100
#now let us simulate a coin toss
print("let's simulate a coin toss")
t = str(input("H for heads, T for tails:"))#now why did it show error when we did char? 
a = random.randint(0,2)
if 1 >= a >= 0:
    print("Heads")
    output = "H"
else:
    print("Tails")
    output = "T"
if t == output:
    print("You win")
else:
    print("You lose")
del output,t,a #deleting the variables we created to free up memory
#let's make 6 pgase dice
print (random.randrange(1,7)) #randrange is like range but it gives a random number in the range like a 6 pgase dice
dice_1 =random.randrange(1,7)
dice_2 =random.randrange(1,7)
print("the sum of the two dice is",dice_1 + dice_2)
del dice_1,dice_2