#what are if conditions?
#what if we only want something to happen if a critea is met
#marvels adgentures is pg13; so you should be 13 or older to watch, let's run code to check for that
print("Gimme your year of birth")
birth_year = int(input())
current_year = 2025
age = current_year - birth_year
if age< 13:
    print("Womp womp, you're not old enough ;-;, come back when you're older")
else:
    print("Congraulations you're old enough to watch marvel movies")
print("\"Nice time, may you have\" - Yoda") #notice hwo we use an if else pair? now if can exist on it's own, but else needs an if
#so does else if, now these are used in cases of conditions , but odn't go overbaord ther're switch statements for tons of conditions
