balance = 999999 
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12

lb = balance / 12
ub = (balance * ((1 + monthlyInterestRate) ** 12)) / 12.0

#print lb
#print ub

tBalance = balance

#while True:
for i in range(50):
    tBalance = balance    
    guessPayment = (ub + lb) / 2
    
    #print "Guess#" + str(i) + ":" + str(guessPayment)
    
    for m in range(1,13):        
        tBalance -= guessPayment 
        interest = tBalance * monthlyInterestRate
        tBalance += interest 
        #print "Month: " + str(m)
        #print "Minimum monthly payment: " + str(round(guessPayment, 2))
    
    #print "Remaining tBalance: " + str(round(tBalance, 2))   
    
    if abs(tBalance) <= 0.01:
        break;
    elif tBalance > 0:
        lb = guessPayment
    elif tBalance < 0:
        ub = guessPayment

#print "Remaining tBalance: " + str(round(tBalance, 2))
print "Lowest Payment: " + str(round(guessPayment,2))