#write code that sums first 10 integers
'''
sum = 0
for i in range(11):
    print(i)
    sum = sum + i
print(sum)'''
#now what if we want it to take input of n and print n many?
n=int(input("Give me a number, i'll find the sums of thos emany numbers"))
sum = 0
for i in range(n+1):
    print(i)
    sum = sum + i
print(sum)