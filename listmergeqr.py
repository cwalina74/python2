
def listmerger(firstlist, secondlist):
    firstlist.extend(secondlist)
    return firstlist


D = ["caroline", "matt"]
L = ["dave"]
print(listmerger(D,L))

