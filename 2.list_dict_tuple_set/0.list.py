# filename: list

list01 = []
print(type(list01))

# str01 = "abcdefg"
# print(str01[1:])

list02 = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in range(len(list02)):
#     print(list02[i])
#
# n = 0
# while n < len(list02):
#     print(list02[n])
#     n += 1

# slice list.
print(list02[0:len(list02)])

# check metadata.
print(list02[4])

# modify metadata.
list02[2] = 30
print(list02)

# list's append.
list02.append(9)
print(list02)

list02.append(3.14)
print(list02)

list02.append("PI")
print(list02)

# list's remove.
list02.remove(30)
print(list02)

list02.pop()
print(list02)

# list's insert.
list02.insert(7, 6)
print(list02)