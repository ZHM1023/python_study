# filename: case_traversing_dict.py

def traverdict(tdict):
    for i in tdict.keys():
        print(tdict[i])

dict01 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# traverdict(dict01)



# dict01 = {key:value for key in names for value in scores}
# print(dict01)

# for i in names:
#     dict02[i] = scores[]

def createdict(key_list01, value_list02):
    fdict = {}
    if len(key_list01) == len(value_list02):
        i = 0
        while i < len(key_list01):
            fdict[key_list01[i]] = value_list02[i]
            i += 1
        return fdict
    else:
        print("check your list len.")

names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
print(createdict(names, scores), type(createdict(names, scores)))
