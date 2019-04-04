# filename: case_traversing_list.py

def traverlist(tlist):
    for i in range(len(tlist)):
        print(tlist[i])

traverlist([1, 2, 4, 7, 9])
list01 = [x for x in range(101) if x % 3 == 0 and x % 2 == 0]
traverlist(list01)