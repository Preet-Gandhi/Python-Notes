#reverse digits of given input
a = int(input("Please enter a number and I'll reverse it"))
b = a
last_num =0
rev_number = 0
if a > 0:
    while b>0:
        last_num=b%10
        b=b//10
        rev_number = rev_number*10 + last_num
elif a<0:
    b = abs(a)
    while b>0:
        last_num=b%10
        b=b//10
        rev_number = rev_number*10 + last_num
    rev_number = -1*rev_number
else:
    rev_number=0
print(rev_number)
del a,b,last_num,rev_number
#find factorial of given number
a = int(input("Please put in a positive integer, I'll give you it's factorial"))
n = a
factoral_n_ = 1
if a<0:
    print("Negative numbers can't have factorials")
else:
    while n>0:
        factoral_n_=factoral_n_*n
        n-=1
    print(factoral_n_)

i = 1
factoral_n_ = 1
if a<0:
    print("Negative numbers can't have factorials")
else:
    while i<=a:
        factoral_n_=factoral_n_*i
        i+=1
    print(factoral_n_)
del a,n,factoral_n_,i
#Number of digits
int_ini = abs(int(input("Give me an integer number, i'll tell you how many digits are in it")))
i=1
ref_num = int_ini
while ref_num > 9:
    ref_num = ref_num // 10
    i += 1
print("Your number",int_ini,"has",i,"digits")
ref_num=int_ini
i=1
if int_ini==0:
    i=1
else:
    i=0
    while ref_num >=1:
        ref_num = ref_num / 10
        i += 1
    print("Your number",int_ini,"has",i,"digits")
del int_ini,ref_num,i
#find if a number is a palindrome or not 
#when the 1st and last number of the number is the same
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
