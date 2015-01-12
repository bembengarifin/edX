start = 0
end = 100
print "Please think of a number between 0 and 100!"

divisor = 2

while True:
    guess = (start + end) / divisor     
    print "Is your secret number " + str(guess) + "?"
    inp = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if inp == "h":
        end = guess
    elif inp == "l":
        start = guess
    elif inp == "c":
        print "Game over. Your secret number was: " + str(guess) 
        break
    else:
        print "Sorry, I did not understand your input."        
