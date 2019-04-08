# Author: bavdu
# Email: bavduer.163.com
# Date: 2019/04/07
# Usage: study excel write.


# pip3 install xlrd xlwt xlutils

import xlwt

list01 = [["name", "age", "sex", "score"],
          ["Tom", 21, "Man", 101],
          ["Jerry", 21, "Woman", 60.5],
          ["Hale", 23, "Man", 79],
          ["Role", 30, "Woman", 100]]

# list01 = [["name", "age", "sex", "score"]]
# list02 = ["Tom", 21, "Man", 59.5]
#
# list01.append(list02)
# print(list01, type(list01))

# table = xlwt.Workbook(encoding="utf-8")
# sheet = table.add_sheet("sheet01")
# row = 0
# for data in list01:
#     col = 0
#     for element in data:
#         sheet.write(row, col, element)
#         col += 1
#     row += 1
# table.save("./information.xlsx")


def writable(data, filename):
    table = xlwt.Workbook(encoding="utf-8")
    sheet = table.add_sheet("sheet1")

    row = 0
    for d in data:
        col = 0
        for information in d:
            sheet.write(row, col, information)
            col += 1
        row += 1
    table.save(filename)

writable(list01, "test.xlsx")

