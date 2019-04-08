# Author: bavdu
# Email: bavduer@163.com
# Date: 2019/04/08
# Usage: study create file.

# file write and read.
file = open("./information.txt", "a")
file.write("ni hen shuai.\n")
file.close()


# read file and with example.
with open("./information.txt", "r") as old_file:
    data = old_file.read()
    print(data)

    line1 = old_file.readline()
    print(line1)
    line2 = old_file.readline()
    print(line2)

    line01 = old_file.readlines()
    print(line01)
    print(len(line01))

    for line in range(len(line01)):
        print(line01[line])
# # old_file.close()





