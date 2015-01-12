balance = 4842
monthlyPaymentRate = 0.04
annualInterestRate = 0.2

totalpayment = 0
totalinterest = 0

for m in range(1,13):
    payment = (balance * monthlyPaymentRate)
    totalpayment += payment
    balance -= payment 
    interest = balance * (annualInterestRate) / 12
    totalinterest += interest
    balance += interest 
    print "Month: " + str(m)
    print "Minimum monthly payment: " + str(round(payment, 2))
    print "Remaining balance: " + str(round(balance, 2))

print "Total paid: " + str(round(totalpayment, 2))
print "Remaining balance: " + str(round(balance, 2))
