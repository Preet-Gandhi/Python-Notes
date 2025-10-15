#what if we want to print it's a beautiful day.
#well we could enclose it in "" but i don't want to so what?
#that's wehre escape characters come in \
print('It\'s a beautiful day') 
#the character immediatly following a \is considered as a character and displayed as one
print("We're form \"IIT\"Madras") 
#each character we want treated as a string char needs a \ before it
print("My name is Jherald. I'm form Alps")
#what if i want more space between James and I'm -> well we could always add more spaces
#extra spaces are not encouraged, ther's escape character for that "\t"
print("My name is James.\tI'm form Alcatraz")
#much better, muhaha now look at this autrocity
print("My name is Jermmy.\t\tI'm form Alaska") #but now i want to put them in differnt lines
#i don't want to use ''' ''' or """ """ or another print function.... what about \n
print("My name is Jhonathan.\nI'm form askaban")
#now what if we want to store a stirng across multiple lines?
'''
z='a
second line
third line'
print(z)
 this will give us an error?'''
#so we should try to use tripple ' or tripple "
z='''a
second line
third line'''
print(z) #tripple quotes can store multi line strings
'''can also be used for commetning in python >.< that too the whole line sin't commented out'''
