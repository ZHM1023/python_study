# filename: cycle_break.py

# for i in range(1, 101):
#     if i % 3 == 0 and i % 8 == 0:
#         print(i)
#         break

num = 1
while num <= 100:
    if num % 4 == 0 and num % 6 == 0:
        print(num)
        break
    num += 1