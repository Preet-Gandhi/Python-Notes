#replication
s ='good'
print(s*5) #i think it'll print good 5x
print(s[0]*5) #it'll print g 5x

#string comparision
x = 'India'
print(x=='India')
print(x=='india')#i think top one will print true and this one false, singular change in character makes strings not equal
#what if we compare them?
print('apple'>'one')
print('four'<'ten')
#it's possible to compare strings. but wtf , how 
#apple > one. apple is longer and has more characters but not greater. Here the comparision operator works in different manner
#comparision is done character by character -> a compared to o. Is a greater than o? false. thus entire comparison is false
#in second case t is greater than f thus the statmenet is true
#if first letters are equal it comapres the second, then third , then so on letters. 
#what if one runs out of letters?
print('abcdef'<'abcde') #False. thus ig it counts blank/nothing spaces and anything by default is greater

#string indexing, rather than normal indexing what if we give negative numbers? -1, -2, -3, -4, -5, -6
s = 'python'
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])
#we just get letters of string in reverse order
#-1 acesses last letter, -2 is second last and so on. this is negative indexing

s='hjoiaehfoauebfoaiefhbaiefubaeofihaeo'
#print(s[100]) would give error, out of range (meaning hundredth character not exist. so it own't print non existant characters)
#how to know characters in string? (like form 0 to x)
#length comand
print(len(s)) #this starts count at 1 , so if we want 36th character we'll need to use [35] as indexing starts at 0
print(s[35])