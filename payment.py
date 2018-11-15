import pandas as pd
import os
import xlrd


def open_file(fileNames):
	os.chdir('C:\\Users\\a206345\\Desktop\\CodeCrowd\\Payments\\NDS_Card_Payments')
	file_list = os.listdir()
	print(file_list)

	for i in file_list:
		book = pd.ExcelFile('C:\\Users\\a206345\\Desktop\\CodeCrowd\\Payments\\NDS_Card_Payments\\' + i)
		print(book.sheet_names)
		for n in book.sheet_names:
			sheet = book.parse(n)
			print(sheet)

        

if __name__ == "__main__":

	fileNames = os.listdir()
	open_file(fileNames)

	