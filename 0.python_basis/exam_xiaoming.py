# filename: exam_xiaoming
# Author: bavdu
# Date: 2019/04/02
# Usage: get xiaoming's grade.

# grade2018 = 72
# grade2019 = 85
# print(type(percentage))
# print(percentage)

grade2018 = int(input("please your student's grade(Notice:2018's grade):"))
grade2019 = int(input("please your student's grade(Notice:2019's grade):"))
percentage = (grade2019-grade2018)/grade2018
print("this is student grade between latest year grade improve: %.1f%%" %(percentage*100))