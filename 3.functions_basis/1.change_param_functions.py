# filename: change_param_functions.py

# def factor(*param):
#     for i in param:
#         flist = []
#         for j in range(1, i+1):
#             if i % j == 0:
#                 flist.append(j)
#         print(flist)
#
# factor(10, 12, 14, 18)

def factor(*param):
    for i in param:
        flist = [x for x in range(1, i+1) if i % x == 0]
        print(flist)
factor(12, 14, 16)