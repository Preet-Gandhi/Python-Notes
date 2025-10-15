#three new key words -> break, continute, pass
#we have a problem statement -> we accept email id, then we only want to print it's username
#so we stop before we reach @ 
email = input("gime email")
for c in email:
    if c == "@":
        break    
    print(c, end="")
#now we want domain name
email = input("\ngime email")
for c in email:
    if c == "@":
        print(" ")
        continue    #if condition exits, it's true, we hit continue, it just skips the iteration, jumps to next iteration from @ to g
    print(c, end="")
print("") 
#what if we want to sort numbers 1-10 into 2 catagories
#those which are and those which aren't divisible by 3
for x in range(1,11):
    if x % 3 ==0:
        print(x)
    else: #else block cna't be left blank, so what to put in? -> pass (just keesp on going)
        pass #here a comment can't act as pass, as a computer just ignores it, where as pass statement mens continue on