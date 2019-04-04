
def factor001(nums):
    flist = []
    for i in range(1, int(nums) + 1):
        if int(nums) % i == 0:
            flist.append(i)
    return flist


def factor002(*param):
    for i in param:
        flist = []
        for j in range(1, i+1):
            if i % j == 0:
                flist.append(j)
        print(flist)