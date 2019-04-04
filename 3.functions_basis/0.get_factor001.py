# filename: get_factor001.py

# def factor():
#     for i in range(1, 11):
#         if 10 % i == 0:
#             print("10's factor include: ", i)
#
# factor()

# def factor(nums):
#     for i in range(1, int(nums)+1):
#         if int(nums) % i == 0:
#             print("%d's factor include: %d" %(int(nums), i))
#
# factor("10")

def factor(nums):
    flist = []
    for i in range(1, int(nums) + 1):
        if int(nums) % i == 0:
            flist.append(i)
    return flist

print(factor(20))