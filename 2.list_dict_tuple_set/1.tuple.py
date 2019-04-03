# filename: tuple.py

tuple01 = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple01, type(tuple01))

tuple02 = (1, 2, 3, [], 9, 6)
print(tuple02)

tuple02[3].append(1)
print(tuple02)

# tuple02[3] = [1, 2, 3, 4, 5, 6]
# print(tuple02)
for i in range(2,11):
    tuple02[3].append(i)
print(tuple02)

# get list[index=4].
# a = tuple02[3]
# print(a)
# print(a[4])
print(tuple02[3][4])