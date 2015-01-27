def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
 #   return 200*math.e**(math.log(0.5)/14.1 * x)
#    return 60*math.e**(math.log(0.5)/55.6 * x)
    
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    '''
    total = 0.0
    i = start
    while i < stop:
        #print str(i) + " - " + str(f(i))
        total += (f(i) * step)
        i += step
    return total
    '''
    total = 0
    for x in frange(start, stop, step):
        #print str(x) + " - " + str(f(x))
        total = total + f(x) * step
    return total



def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step        
        
#print f(5.0)        
    
print radiationExposure(0,5,1)
print radiationExposure(5,11,1)
print radiationExposure(0,11,1)
print radiationExposure(40,100,1.5)