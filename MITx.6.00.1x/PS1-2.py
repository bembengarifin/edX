s = 'azcbobobegghakl'

pos = 0
end = len(s)

f = 0

while True:
    found = s.find('bob', pos, end)
    if found != -1:
        #print found
        f += 1
        pos = found + 1
    else:
        break            

print "Number of times bob occurs is: " + str(f)