# filename: andornot.py

print(2 > 3)
print(3 < 2)

print(32 > 28)

var01 = "hello world"
var02 = "hello kitty"
print(var01 + var02)

print(2 > 3 or 1 < 2)
print(not 2 > 3)





# if.
if 3 < 2:
    print("3 less than 2.")
else:
    print("3 more than 2.")

print("#*#"*20)

if 10 % 2 == 1:
    print("10 / 2 = 5")
elif 10 % 5 == 0:
    print("10 / 5 = 2")
elif 10 % 3 == 1:
    print("10 / 3 = 3.333")

print("#*#"*20)

if 10 % 2 == 0:
    if 10 % 5 == 0:
        print("10%5=10%2=0")
    else:
        print("####")
else:
    if 10 % 3 == 1:
        print("10%2 < 10%3")
    else:
        print("####")






