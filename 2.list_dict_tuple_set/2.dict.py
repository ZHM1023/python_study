# filename: dict.py

dict01 = {}
print(dict01, type(dict01))

# add iterms.
dict01["Tom"] = 98
print(dict01)
dict01["Jerry"] = 99
print(dict01)
dict01["Bob"] = 100
print(dict01)

# delete iterms.
dict01.pop("Bob")
print(dict01)

# modify iterms.
dict01["Jerry"] = 100
print(dict01)

# check iterms.
name = "Tom"
print("%s's grade is: " %name, dict01[name])

# check iterms's key;
for i in dict01.keys():
    print("%s's grade is: \t" %i, dict01[i])

# check iterms's value;
for i in dict01.values():
    print(i)