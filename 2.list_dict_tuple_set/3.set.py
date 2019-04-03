# filename: set.py

list01 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
set01 = set(list01)
print(set01)

list02 = [3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 7, 7, 8, 8, 9, 9, 0, 0]
set02 = set(list02)
print(set02)

# add iterms.
set02.add(2)
print(set02)

# delete iterms.
set02.pop()
set02.pop()
set02.pop()
print(set02)

set02.remove(9)
print(set02)

# jiaobing ji.
set03 = {1, 2, 3, 4, 5, 6, 7, 8}
set04 = set(list02)
print(list02)

# jiaoji.
jiaoji = set03 & set04
print(jiaoji)

# bingji.
bingji = set03 | set04
print(bingji)