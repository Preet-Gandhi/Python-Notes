#make multiplication table
ori_num = int(input("What numbers multiplication table would you like th know?\n"))
multi_num = int(input("What number would you like to know the table to\n"))
'''
for i in range(multi_num+1):
    print(ori_num,"*",i,"=",ori_num*i)'''
#how to get rid of that pesky zero?
#simple (1,last value) prints form 1 to n-1)
for i in range(1,multi_num+1):
    print(ori_num,"*",i,"=",ori_num*i)
