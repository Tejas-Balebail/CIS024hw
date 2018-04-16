
import sys
import sorthelper
l = []

for x in range(1,len(sys.argv)):
    l.append(sys.argv[x]) 
    
my_l = sorthelper.sortNumbers(l)

print 'The sorted list is: ',my_l

### END CODE