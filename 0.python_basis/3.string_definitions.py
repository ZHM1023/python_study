# filename: string_defintions

var01 = "this is string."
var02 = "18640448956"
var03 = "this's FE"
var04 = 180

var01_len = len(var01)
print(var01_len, type(var01_len))

print("this is my phone: %s" %(var02)) # string replace chr.
print("this is my tall: %d" %(var04))
print("this is my tall: ", var04)

name = "bavduer"
phone = 18640405689
print("my name is: %s, my phone is: %d" %(name, phone))

# slice

var001 = "this is my girl friend."
var001_len = len(var001)
print(var001_len)

# slice: var001[1:23]
print(var001[1:23])
print(var001[0])
print(var001[0:3]) # 0 <= x < 3
print(var001[0:4]) # 0 <= x < 4


print(var001[11:])
print(var001[:len(var001)])
print(var001[:])

print(var001[-1])
print(var001[-12:])