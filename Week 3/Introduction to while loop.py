#let's make a small program this is an example of a program which makes you enter a value until
#a certain condition is satisfied. here we wannted the independence. but notice how it's tedious and infinite
#nexted if looops if we try to get unlimited inputs?... i'm sure ther's a better way...
#D_o_I = str(input("When did India get it's independence?\n ")) -> var declaration and input
'''if D_o_I == "1947": -> check if true
    print("That's correct... GOOD JOB!! :p\n")
else: what to do if false
    print("Bruh")
    print("such a simple fact :C") -> but what if we want tog ive them a second chance?
    print("You have one last chance to answer correctly.") -> give second chance
    D_o_I = str(input("When did India get it's independence?") -> read second input
    if D_o_I == 1947: -> check second input (must be in else statement)
        print("LETS GOOOO !!!")
    else: -> finaly tell them the answer after another worng attmept 
        print("You really don't know this simple fact :C")
        print("The correct answer is 1947")'''
D_o_I=str(input("When did India get it's independence?\n "))
#what if we wrote piece of code which allows unlimited allows until right answers?
#well the're something called loops. Here's an example of a while loop; happens until condition is met
while (D_o_I != "1947"):
    print("YOU'VE ANSERD WRONG... BE DAMMED TO ETERNAL ANSWERING")
    D_o_I = str(input("Carefully.... What's the year? of India's independence?\n"))
print("Finally, I can rest now... thank you ... it's been 2 billion system cycles")
