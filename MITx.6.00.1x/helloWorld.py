import sys

print "hello world"

print sys.version

None

print None

happy = 3

if happy > 2:
    print "hello world"



varA = -1
varB = 0


if (type(varA) == str or type(varB) == str):
    print "string involved"
elif (varA > varB):
    print "bigger"
elif (varA == varB):
    print "equal"
elif (varA < varB):
    print "smaller"    

i = 2
while i <= 10:
    print i
    i += 2
print "Goodbye!"

print "Hello!"
i = 10
while i >= 2:
    print i
    i -= 2

end = 6
s = 0
counter = 1
while counter <= end:
    s += counter
    counter += 1
print s

num = 10
for num in range(5):
    print num
print num

for letter in 'hola':
    print letter
    
for i in range(2, 11, 2):
    print i 

print "Goodbye!"


print "Hello!"
for i in range(10, 1, -2):
    print i 

end = 6
s = 0   
for i in range(1, end + 1):
    s += i
print s

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1
    
     
#x = 25
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#
#while guess <= x:
#    if abs(guess**2 -x) >= epsilon:
#        guess += step
#
#if abs(guess**2 - x) >= epsilon:
#    print 'failed'
#else:
#    print 'succeeded: ' + str(guess) 
    
x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)    