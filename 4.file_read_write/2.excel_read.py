# Author: bavdu
# Email: bavduer@163.com
# Date: 2019/04/07
# Usage: study read excel file.

import xlrd

# with xlrd.open_workbook("./test.xlsx") as table:
#     sheet = table.sheets()[0]
#     row = sheet.nrows
#     col = sheet.ncols
#
#     data = []
#     for r in range(row):
#         row_data = []
#         for c in range(col):
#             row_data.append(sheet.cell_value(r, c))
#             print(row_data)
#         data.append(row_data)
#     print(data)

def rdtable(filexlsx):
    with xlrd.open_workbook(filexlsx) as table:
        sheet = table.sheets()[0]
        row = sheet.nrows
        col = sheet.ncols

        data = []
        for r in range(row):
            rows_data = []
            for c in range(col):
                rows_data.append(sheet.cell_value(r, c))
            data.append(rows_data)
        return data

print(rdtable("./information.xlsx"))