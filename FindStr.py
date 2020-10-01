import sys

# build an array which describes how far away each character is from the next
def getDifferences(x):
    ccount=[]
    for i in range(0,len(x) - 1):
        ccount.append(ord(x[i+1]) - ord(x[i]))
    return ccount

# make sure we have the correct number of arguments
try:
    # get the search string and the difference array of the search string
    s=sys.argv[1]   
    c=getDifferences(s)
    
except IndexError:
    sys.stdout.write("usage: %s\"search string\" file...\n" % sys.argv[0]) 
    sys.exit(-1)

for fname in sys.argv[2:]:
    f=open(fname,"rb").read()
    print "looking for %s in %s" % (s, fname)	

    # loop through the file checking if each character is the beginning of a pattern
    # that matches the difference values
    for i in range(0,len(f) - len(s)):
        x=getDifferences(f[i:i+len(s)])
        if x == c:
            print "\tmatch in %s at offset 0x%2x" % (fname,i)
