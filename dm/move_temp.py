import numpy as np

from xlrd import open_workbook

book = open_workbook('CAMEO Ontology 033117.xlsx',on_demand=True)
sheet = book.sheet_by_name("Move Codes")
num_rows = sheet.nrows - 1
curr_row = 0

data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

column = [i[3] for i in data][1:]
book.close()
print(np.unique(column))

