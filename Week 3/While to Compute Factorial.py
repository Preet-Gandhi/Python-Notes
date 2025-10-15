#now we'll try to find the factorial of a number... using a loop it sounds very complicated... 
#it'll probally ahve multiple revisions... so mabey while loop is good?
a = int(input("Give me a number and I'll find it's factorial."))
product = 1
b = 1
if a<0:
     print("Factorial of negative numbers doesn't exist.")
     quit()
while a >= b:
     product= product * b
     b +=1
print("The factorial of",a,"is:",product)
del a,b,product

#that was my attempt; let's see what the prof does
print("Enter a number")
n=int(input())
answer = 1
#answer=answer*2
#answer=answer*3
#and so on until answer = answer*n
#mabey this can be while loop?
#print(answer)
#this is manual computing, well we don't want that. 
#now we keep the first 3 lines the same but. 
i=1 #to be a counter to keep track of how many times we multiply
while i<=n:
    answer=answer*i
    i=i+1
print(answer)
#here i grows and attemps to exceed i, but one the wya it's multiplied into answer each time
#thus it acts like answer = 1*2*3*4*...n thus answer beocems factorail and condition is met for exit of loop
del n,answer,i