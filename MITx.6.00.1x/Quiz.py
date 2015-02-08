import math

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

#for x in range(0,10):    
#    print Square(x)

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    #return 0
    #import math
    #return math.log(x, b)
    power = 0
    applied = b
    while x >= applied:
        applied *= b
        power += 1
    return power

def myLogRec(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    def recur(x, b, c):
        if x < b:
            return c
        else:
            return recur(x/b, b, c + 1)
            
    return recur(x, b, 0)
    
def test(expected, actual):       
    #assert expected == actual, "test failed for expected {0} vs actual {1}".format(expected, actual)
    if expected != actual:
        print "test failed for expected {0} vs actual {1}".format(expected, actual)
    else:
        print "test is successful for expected " + str(expected)

#test(4, myLog(16,2))
#test(2, myLog(15,3))
#test(4, myLogRec(16,2))
#test(2, myLogRec(15,3))

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    maxLen = len(s1) if len(s1) > len(s2) else len(s2) 
    result = []
    if maxLen == 0:
        return ""
    else:
        for i in range(0, maxLen):
            if i < len(s1):
                result.append(s1[i])

            if i < len(s2):
                result.append(s2[i])        

    return ''.join(result)
    
#test("aebfcgdhi", laceStrings("abcd", "efghi"))  

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            pass
        if s2 == '':
            return out + s1[0:]
        else:
            return helpLaceStrings(s1[1:], s2[1:], out + s1[:1] + s2[:1])
    return helpLaceStrings(s1, s2, '')
    
#test("aebfcgdhi", laceStringsRecur("abcd", "efghi"))      
#test("kfgnqptn", laceStringsRecur('kgqtn', 'fnp'))     


def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    """
    #code below doesn't work
    sizes = [6, 9, 20]

    # 0,1,2
    if (((n % sizes[0]) % sizes[1])) % sizes[2] == 0: return True
        
    # 0,2,1
    if (((n % sizes[0]) % sizes[2])) % sizes[1] == 0: return True
    
    # 1,0,2
    if (((n % sizes[1]) % sizes[0])) % sizes[2] == 0: return True

    # 1,2,0
    if (((n % sizes[1]) % sizes[2])) % sizes[0] == 0: return True
    
    # 2,0,1
    if (((n % sizes[2]) % sizes[0])) % sizes[1] == 0: return True
    
    # 2,1,0
    if (((n % sizes[2]) % sizes[1])) % sizes[0] == 0: return True
    """
    #http://mathproblems.info/prob9s.htm
    #For any desired number if it is divisible by 3 it can easily be made with 6 and 9 packs, except if the number is 3 itself. If you can't use all six packs then use one 9 pack and you can do the rest with six packs.
    #If the number is not divisible by 3 then use one 20 pack. If the remaining number is divisible by 3 then use the above method for the rest.
    #If the number still isn't divisible by 3 use a second 20 pack. The remainder must be divisible by 3, in which case use the 6 and 9 packs as above.         

    if n >= 6 and n % 3 == 0: return True
     
    i = 1
    while n > (20 * i):
        if (n - (20 * i)) % 3 == 0:
            return True;
        i += 1
        
    return False
    
    """

    for s in range(len(sizes)):
        # test single
        print s    
    """

#test(True, McNuggets(62))
#test(True, McNuggets(15))    
#test(False, McNuggets(16))    
#test(True, McNuggets(236))
#test(True, McNuggets(146))
#test(False, McNuggets(17))
#test(True, McNuggets(45))
#test(True, McNuggets(133))
#test(False, McNuggets(28))
#test(True, McNuggets(239))
#test(True, McNuggets(32))
#test(False, McNuggets(1))    
#test(True, McNuggets(100000))    

def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        print abs(f(guess) - guess)
        print epsilon
        if f(guess) - guess < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess


#def sqrt(a):
#    def tryit(x):
#        return 0.5 * (a/x + x)
#        #return x * x - 3 * x + 4
#    return fixedPoint(tryit, 0.0001)

def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt(a):
    return fixedPoint(babylon(a), 0.0001)

print sqrt(4)
