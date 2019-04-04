# filename: cycle_functions.py
# 1+2+3+4+5+6+7+8+9+10+....+90+91+92+93+94+95+96+97+98+99+100

# sum = 0
# for i in range(101):
#     sum += i
# print(sum)

def sum(param):
    if type(param) != int:
        print("please your input int type.")
    if param == 1:
        return param
    return sum(param - 1) + param

# sum(100) = sum(100 -1) + 100
# sum(100 -1) + 100 = sum(99) + 100 = sum(99 -1) + 99 + 100
# sum(99 -1) + 99 + 100 = sum(98) + 99 + 100
#                         sum(98) = sum(98 -1) + 98 +99 +100

print(sum(100))
print(sum("100"))