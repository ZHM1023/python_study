# filename: case_traversing_dict.py

def traverdict(tdict):
    for i in tdict.keys():
        print(tdict[i])

dict01 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# traverdict(dict01)


names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
# dict01 = {key:value for key in names for value in scores}
# print(dict01)

# for i in names:
#     dict02[i] = scores[]
dict02 = {}
i = 0
while i < len(names):
    dict02[names[i]] = scores[i]
    i += 1
print(dict02)


