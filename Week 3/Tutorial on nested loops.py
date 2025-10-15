#we can have any variation of nested looping -> for,for; for,while; while,while; while,for
#find all prime less than entered number
enter_num = int(input(f'Give me a number an I\'ll give you all the prime factors less than it' ))
flag = False
if enter_num<=2:
    print(f'{enter_num} is not a prime number')
for i in range(2,enter_num): #helps us find all numbers lesser than inputed vlaue
    for j in range(2,i): #now why start with 2, well if not we'd ahve 0 or 1 
        if(i%j == 0 and i != j): #0 by anything is 0, everyting is by 1 so they'd 
            flag=True #give errors
            break #so it doen't go to next value of j and overide true flag
        else:
            flag = False
    if flag ==False: 
        print(f'{i} is a prime number')
#find loss and profit of each trader working in trading firm
employ_id = str(input("Give me your employ ID"))
net_total = 0
while employ_id != "-1":
    transaction_amount = int(input("Give me your transaction amount"))
    while transaction_amount != 0:
        net_total= net_total+transaction_amount
        transaction_amount = int(input("Give me your transaction amount"))
    print(f'Employ ID{employ_id} has made a net total of {net_total}')
    net_total=0 
    employ_id = str(input("Give me your employ ID"))
#Find day wise total rainfall for entered duration of time 
days = int(input("Enter number of days we'll check rainfall for"))
daily_rainfall = 0
total_rainfall = 0
for i in range(1,days+1):
    daily_rainfall=int(input(f'Enter in rainfall for day {i}'))
    while daily_rainfall != -1:
        total_rainfall = total_rainfall + daily_rainfall
        daily_rainfall=int(input(f'Enter in rainfall for day {i}'))
    daily_rainfall = 0
    print(f'Total rainfall for day {i} is expected to be {total_rainfall} unit of measurements')
    total_rainfall = 0
#now find longest word length
word = input("Give me a sentence and I'll give you the length of the longest word in it: ")
max_length = 0
while (word != "-1"):
    count = 0
    for letter in count:
        count = count + 1
    if count > max_length:
        max_length = count
    word=input("enter a word:")
print("The length of the word is %s" % max_length)