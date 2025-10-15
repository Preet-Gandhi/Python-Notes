#now what about the differnces and advantages of for and while loops
#we have the factorial code 
a = int(input("Please put in a positive integer, I'll give you it's factorial\n"))
n = a
factoral_n_ = 1
if a<0:
    print("Negative numbers can't have factorials\n")
else:
    while n>0:
        factoral_n_=factoral_n_*n
        n-=1
    print(factoral_n_)
#now let's make it a for loop
factoral_n_=1
n = a
if n <0:
    print("Negative numbers can't have factorials\n")
else:
    for i in range(1,n+1):
        factoral_n_=factoral_n_*i
    print(factoral_n_)
del a,n,factoral_n_,i
#see how much shorter that was and easier? 
#they do the same thing, but how do we dcided which loop to know?
#now if we know if the loop runs for n times we use for loop
#if we don't know how many times the loop is going to turn we should use while loop
#while is the more generic form, in factorial we know number of iterationss o it's more suitable 
#calculate number of digits
num=abs(int(input("Give me an integer number, i'll tell you how many digits are in it\n")))
n = num
digits = 1
while n>9:
    n=n//10
    digits+=1
print(f"Your number {num} has {digits} digits") 
#now we could use a for loop here as well or could we???
#answer no! we don't know how mny times it will run, we're lost
#mabey we can make a work around souition
#what if we convert num into string?
digits=0
n_string = str(num)
for i in n_string:
    digits+=1
print(digits)
del num,n,digits,n_string
#reversal of digits is using for function -> use for each, we'll have to convert into string
num = int(input("Give me number and i'll reverse it"))
abs_string_num = str(abs(num))
rev = ""
for i in abs_string_num:
    rev = i + rev #i will be the values in abs_str_num, concationan will append rev to behind it
if num >0:
    print(rev)
else:
    print("-"+rev)
del num,abs_string_num,rev #not ideal way to write
#find it number is palandrome 
num = int(input("Give me a number and I'll determine if it's a palandrome or not."))
orignal_num = num
rev = 0
last_digit = 0
while orignal_num > 0 :
    last_digit = orignal_num % 10
    rev = rev*10 + last_digit
    orignal_num = orignal_num // 10
print(rev)
if rev == num:
    print("It's a palandrome!!!")
else: 
    print("Booo Hooo, it's not a palandrome!!! ;-; ") 
#now inject for statement... 
num = int(input("Give me a number and I'll determine if it's a palandrome or not."))
#c = 0
str_num = str(abs(num))
for i in range(len(str_num)//2):
    if str_num[i] == str_num[-(i+1)]:
        c = True
    else:
        c=False
        break
if c:
    print("It's a palandrome!!!")
else:
    print("It's not a palandrone, r you gona cry?")
#it's not possible to deifne for functiona s we cna't predict number of iterations to reverse the number so we contert it itno a string and go forward
''' else: c== False
if c == True:
    print("It's a palandrome!!!")

'''
'''
rev = 0
last_digit = 0
while orignal_num > 0 :
    last_digit = orignal_num % 10
    rev = rev*10 + last_digit
    orignal_num = orignal_num // 10
print(rev)
if rev == num:
    print("It's a palandrome!!!")
else: 
    print("Booo Hooo, it's not a palandrome!!! ;-; ")
'''