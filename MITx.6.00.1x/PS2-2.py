balance = 3329 
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12
guessPayment = 0

while True:
    tBalance = balance    
    guessPayment += 10

    for m in range(1,13):
        tBalance -= guessPayment 
        interest = tBalance * monthlyInterestRate
        tBalance += interest 
        #print "Month: " + str(m)
        #print "Minimum monthly payment: " + str(round(guessPayment, 2))
        #print "Remaining tBalance: " + str(round(tBalance, 2))    

    if tBalance <= 0:
        break

#print "Remaining tBalance: " + str(round(tBalance, 2))
print "Lowest Payment: " + str(guessPayment)