def get_row_column(file_xls_dir, sheetName):
    import xlrd
    file = xlrd.open_workbook(file_xls_dir)
    sheet = file.sheet_by_name(sheetName)
    numRows = sheet.nrows
    numCols = sheet.ncols
    return numRows, numCols


