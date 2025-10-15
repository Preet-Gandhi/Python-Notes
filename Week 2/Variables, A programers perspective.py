#dan
dan_bank_balance = 100000 #this is his income counts as +ve
ram_bank_loan = 500000 #this is his loan, counts as negative
#lakshman
lakshman_bank_balance = 2000000
lakshman_bank_loan = 1000000
#net
net_income = dan_bank_balance + lakshman_bank_balance #total income between brothers
net_loan = ram_bank_loan + lakshman_bank_loan #total loan between brothers
#orignaly it was all a,b,c,d,e,f. that'd be so confusing. so we use variables. 
final_value = net_income-net_loan #net resultant of loans + balance 
print("The family has net value of",final_value,"per month")
#notice how the vars make it easy to remember everything? like containers, their values can be changed
#your variables should be self explanitaory and you should add comments
#add comments cause you will forget, and you will wonder what on earth you were doing.