# filename: variable_defind

var01 = "string"
# print(var01)
# print(type(var01))
# print(len(var01))

print("var01's value: ", var01)
print("var01's type: ", type(var01))
print("var01's lenght: ", len(var01))


a = b = 0
a, b = 12, 78
print(a,b)

a, b = b, a
print(a,b)