#profess goes thorugh s[0] ... s[len(s)-1]
s="VIBGYOR"
for c in s:
    print(c)
for i in range(7):
    print(s[i])
#let's say we have 2 prothers sharat and tanmey, they can wear vibgyor colors; what are all combos
t = s
count = 0
for i in range(7):
    for j in range (7):
        print(s[i],t[j])
        count +=1
print(f'The number of ways S and T can wear 7 colours is {count}')

#this is a nested for loop
