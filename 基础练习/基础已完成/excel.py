import xlrd
xlsfile = r"C:\Users\小光\Desktop\中控实习\强化学习复现\滨盛路建业路数据\信号平台取数据\green_occ.xls"
book = xlrd.open_workbook(xlsfile)
sheet0 = book.sheet_by_index(0)
sheet_name = book.sheet_names()[0]
cell_value1 = sheet0.cell_value(1,5)
print(cell_value1)