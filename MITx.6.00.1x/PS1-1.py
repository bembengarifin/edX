s = 'azcbobobegghakl'

vw = 0
for letter in s: 
    if letter in ['a', 'e', 'i', 'o', 'u']:
        vw += 1
    
print "Number of vowels: " + str(vw)