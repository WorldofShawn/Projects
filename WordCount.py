fname = input ("Type in file name ")
try:
    fhandle=open(fname)
except:
    print ("Invalid file name or cannot be found")
    quit()

Histo=dict()

for line in fhandle:
    words=line.split()
    
    for name in words:
        Histo[name]=Histo.get(name,0)+1

#print (Histo)
for n,c in Histo.items():
    print (n,c)