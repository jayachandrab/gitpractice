import xlrd 
  
# Give the location of the file 
loc = ("SampleData.xlsx") 
  
# To open Work(book 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
res = len(wb.sheet_names())
print(wb.sheet_names())
print(sheet.nrows)
print(sheet.ncols)
# For row 0 and column 0 
print(sheet.cell_value(0, 0))
print(sheet.cell_value(0, 1))
print(sheet.cell_value(0, 1))
for col in range(sheet.ncols):
    print(sheet.cell_value(2,col))


for row in range(1, sheet.nrows):
   
    for col in range(sheet.ncols):
        
        print(sheet.cell_value(row,col), end =" \t"),
    print()
        
print("finish reading excel file")
