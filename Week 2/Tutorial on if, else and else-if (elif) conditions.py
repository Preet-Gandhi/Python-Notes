#let's use if, else and elif conditions in python
# find if number is even or od?
a = int(input("Give me an integer and i'll tell you if it's even or odd: \n"))
if a % 2 == 0:
    print(a,"is an even integer")
else:
    print(a,"is an odd integer")
del a
#now find if last digits of number ends with 0 or 5 or any other number
num = int(input("Give me a number and i'll tell you it's last digits ( well sorta tell you)\n"))
if num % 10 == 0:
    print("The last digit of",num,"is 0")
elif num % 10 == 5:
    print("The last digit of",num,"is 5")
else:
    print("The last digit of",num,"is neither 0 nor 5")
del num
#now... let's see if you can build your own grading system... A >= 90, 90 > B >= 80 , 80 > C >= 70, 70 > D >= 60, E < 60
grade_number = int(input("Give me your marks range/percentile/percentage(must be out of 100 or u'll be unhappy) \n"))
if grade_number < 0:
    print("you scored negative points? caught cheating and didn't know anything... smh")
elif grade_number >= 90:
    print("You got an A! Amazing job!")
elif 90 > grade_number >= 80:
    print("You got a B! Great job!")
elif 80 > grade_number >= 70:
    print("You got a C! Good job!")
elif 70 > grade_number >= 60:
    print("You got a D! You passed but you can do better!")
elif 60 > grade_number >= 0:
    print("You got an E! You failed, better luck next time!")
del grade_number #notice how i didn't use an and statment even tho ic ould bave put 60 > grade_number and grade_number >= 0
#this is because python allows us to chain comparisions (obv what's evaluated first depends on pythons order of operations)
#now let's turn a flow chart into code
print("So you want to travel form city A to city B?\n")
time = int(input("How many hours do you have to travel? \n"))
Longer = int(input("Define longer:"))
if(time>Longer):
    print("So... you've chosen the longer route?")
    price = int(input("What price range do you have in mind? \n"))
    higher = int(input("Define higher:"))
    if(price > higher):
        print("You can travel by Train")
    else:
        print("You can travel by Coach")
else:
    print("I see how it is, air route...")
    price = int(input("What price range do you have in mind? \n"))
    higher = int(input("Define higher:"))
    if(price > higher):
        print("You can travel by Daytime Flight")
    else:
        print("You can travel by Red Eye Flight")
print("Thanks for using our service!")
del time, Longer, price, higher