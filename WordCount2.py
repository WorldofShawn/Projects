Histo = dict()

fname= input("Input file name :")
try:
    fhandle=open(fname)
except:
    print("Invalid file name")
    quit()

for nameline in fhandle:
    line=nameline.split()
    for name in line:
        if name not in Histo:
            Histo[name]=1
        else:
            Histo[name]=Histo[name]+1
print (Histo)