
import xlwt, xlrd

# write xlsx file's content.
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

# read xlsx file's content.
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

