# import xlrd
# import xlutils.copy
#
# inBook = xlrd.open_workbook('2017.xls', formatting_info=True)
# outBook = xlutils.copy.copy(inBook)
#
#
#
#
# def _getOutCell(outSheet, colIndex, rowIndex):
# 	""" HACK: Extract the internal xlwt cell representation. """
# 	row = outSheet._Worksheet__rows.get(rowIndex)
# 	if not row:
# 		return None
# 	cell = row._Row__cells.get(colIndex)
# 	return cell
#
# def setOutCell(outSheet, col, row, value):
# 	""" Change cell value without changing formatting. """
# 	# HACK to retain cell style.
# 	previousCell = _getOutCell(outSheet, col, row)
# 	# END HACK, PART I
#
# 	outSheet.write(row, col, value)
#
# 	# HACK, PART II
# 	if previousCell:
# 		newCell = _getOutCell(outSheet, col, row)
# 		if newCell:
# 			newCell.xf_idx = previousCell.xf_idx
# 	# END HACK
#
# outSheet = outBook.get_sheet(0)
# setOutCell(outSheet, 5, 5, 'Test')
# outBook.save('2018.xls')
#
def addArrows(location_list):
	string_arrows = ""
	for i in range(len(location_list)):
		string_arrows += str(location_list[i])
		string_arrows += " "
		if i < len(location_list) - 1:
			string_arrows += "-> "
	return string_arrows

list1 = ['Canyon Hills', 'Crescent', 'Anaheim Hills']

print(list1)

updated = addArrows(list1)

print(updated)