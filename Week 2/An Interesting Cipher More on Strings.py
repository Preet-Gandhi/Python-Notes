alpha="abcdeke9iq8er974"
print(alpha[0]) #this prints a
print(alpha[1]) #this prints b
print(alpha[2]) #this prints c 
#thus we see how we can call a character of a variable by its index number
print(alpha[3]) #this prints d
#we can also use vars in indexing
x = 4
print(alpha[x]) #this prints e
print(alpha[x+1]) #this prints k
print(alpha[x-1]) #this prints d , other mathmatical functiosn can also be used
del x
#we can also use negative indexing
#we get error if we use negative indexing with a variable
#but if we were to do
print(len(alpha)) #this prints 16
#now we can use the length and do this
i = 16
y = 15
print(alpha[y%i])#now if our value inside the [] is outside of range, it'll automaticly become in range again
#max of indexing is 15 so at y = 15 we get 15 but if y = 16 or above it starts with 0 and increases
del i,y,alpha
#now lets say we want to shift the letters in a strying by n places in the alphabet
alphabet="abcdefghijklmnopqrstuvwxyz"
a = "preet" #now let's say i want to shift this one to the right
#so it should be qsffu
t = ""
i=0
print(alphabet.index(a[0])) #this gives an error as P is not in the alphabet string; this gives us index of p in alphabet
#but we want one ahead of it so....
print(alphabet[(alphabet.index(a[0])+1)%26]) #now wwe take a0's index in alphabet, add one to it , make sure it's in range, then print alpha (index) value
#we want to append this to t not print it
t=t+alphabet[(alphabet.index(a[i])+1)%26]
t=t+alphabet[(alphabet.index(a[i+1])+1)%26]
t=t+alphabet[(alphabet.index(a[i+2])+1)%26]
t=t+alphabet[(alphabet.index(a[i+3])+1)%26]
t=t+alphabet[(alphabet.index(a[i+4])+1)%26] #notice how it's getting tedious? and how we could use k instead of +1 allowing us to shift in any way?
print(t)#also this is a ceaser cipher (cryptography)
print("hellow")