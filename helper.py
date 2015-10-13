import os

from terminaltables import SingleTable


def print_table(table_headers, table_values, table_title=''):
	os.system("cls")

	table_data = [table_headers]

	for i in range(0, len(table_values[0])):
		dataline = []
		for j in range(0, len(table_headers)):
			dataline.append(str(table_values[j][i]))
		table_data.append(dataline)

	table = SingleTable(table_data)
	table.title = table_title
	table.justify_columns = {0: 'right',
							 1: 'right',
							 2: 'right'}
	table.inner_row_border = False
	print(table.table)

 