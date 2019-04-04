# filename: traversing many list.

def traversing(*mlist):
    for tlist in mlist:
        print("tlist is: ", tlist)
        for i in range(len(tlist)):
            print(tlist[i])

list01 = [123, 234, 345, 456]
list02 = [78, 89, 90]
list03 = [23, 34, 45, 56, 67]
traversing(list01, list02, list03)