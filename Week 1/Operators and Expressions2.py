"""Three major types of operators in Python:
1. Arithmetic Operators -> +, -, *, /, //, %, ** (add, sub, multi, divide, floor div, mod, expo)
2. Comparison Operators -> >, <, >=, <=, ==, != (greater than, less than, greater equal, less equal, equal, not equal)
3. Logical Operators -> and, or, not
"""
print("addition: ", 3 + 5)
print("subtraction: ", 10 - 2)
print("multiplication: ", 4 * 7)    
print("division: ", 15 / 7)
#basicly what you'd expect
#what is floor division? it gives int
print("floor division: ", 15 // 7)
#mod gives remainder of a%b a divided by b
#** is obviously a to the power of b
print("modulus: ", 15 % 4) #gives 3
print("exponent: ", 2 ** 3) #gives 8 

#comparison operators, only give boolean values
print(5>10) #false
print(5<10) #true
print(5>=5) #true
print(5<=5) #true
print(5==5) #true double == operant compares and checks if first and second number are equal, bolean value only
print(5!=5) #false

#logical operators (conditions for statements)
print(True and False) #false (only true and true evaluvate to true.  absicly both operants of and must be true)
print(True and True) #true
print(False and True)#false
print (False and False)#false

print(True or False) #true (if even one operant of or is true then it's result is true)
print(True or True) #true   
print(False or True)#true
print (False or False)#false

print(not False) #true (not operator just flips the value of it's operant)
print(not True) #false (not opposite can be used with and withouth brackets)
