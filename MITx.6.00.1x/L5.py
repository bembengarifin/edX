def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    i = 0
    result = 1
    while i < exp:
        result = result * base
        i += 1
    return result
    
for x in range(0, 10):
    print iterPower(2, x)
    
    
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

for x in range(0, 10):
    print recurPower(2, x)
    
def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    elif exp > 0 and exp % 2 == 0:
        return recurPowerNew(base * base, exp / 2) 
    else:
        return base * recurPowerNew(base, exp - 1)    
        

for x in range(0, 10):
    print recurPowerNew(2, x)        