# filename: cycle_continue.py

# for i in range(1, 11):
#     if i % 2 == 0:
#         if i % 4 == 0:
#             continue
#         else:
#             print(i)

i = 0
while i < 11:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
