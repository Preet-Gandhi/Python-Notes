#for loop, keeps on doing everything until i -> 0 to 10, but doesn't include 10
for i in range(10):
    print(i)
    print("Hello World")
#loop as it's ciccular and will repeat until condition is met
#now if and for, and loops can also be included in it
for i in range(10):
    if i% 2 != 0 : #here we could also use != instead of not
        print(i)
#now we print something x many times
a = str(input("Tell me what to print"))
b= int(input("Tell me how many times to print"))
for i in range(b):
    print(a)
