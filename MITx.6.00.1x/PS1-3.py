s = 'ugsllaskhrw'

ls = ""
tmp = ""
for l in s:
    #print ls + "," + tmp + "," + l
    if len(tmp) == 0:
        tmp = l
    elif tmp[-1] <= l:
        tmp += l
    elif tmp[-1] > l:
        if len(tmp) > len(ls):
            ls = tmp
        tmp = l

if len(tmp) > len(ls):
    ls = tmp
        
print "Longest substring in alphabetical order is: " + ls