d=10
newFile = open('mychallengefile.txt','w')

for y in list(range (0,10)):
    for x in list(range(0,d)):
        newFile.write(str(x))
    d = d -1
    newFile.write('\n')

newFile.flush()
newFile.close()
