a,b = 1,2
n = a + b #behaves as we expect
print(n)
#but what if a, b are strings? -> error, a = "abc", b = "def"
# now what if we add 2 strings
s1, s2 = "stringuin1","stringuin2"
s3 = s1 + s2 #concatenation
print(s3)
#it behaves as expected.called concatenation (conconatinate put 2 words together one next to other)
#what if a and b are lists
L1,L2 = [1,2,3],[2,3,9,87,4,5,6]
L3 = L1 + L2
print(L3) #littelry joins the 2 lists based on the order specitifed. 
#data type of of a and b matter. based on that we get output
i1,i2 = 5,22
i3 = i1/i2
print(i3) #gives float value
#what if we do 10+13*2?
i4 = 10+13*2
print(i4) #outcome as expected 36
#python has it's own expression evaluation order/procedure
#called operator precedence (how it solves the expression((coded in)))
#priarity to multiplication over addition
#esponents are ** 