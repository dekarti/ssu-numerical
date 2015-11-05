import os
from terminaltables import SingleTable

def print_table(table_headers,
				table_values,
				table_title='',
				table_view='v'):
	os.system("cls")
	if table_view == 'v':
		table_data = [table_headers]
		for i in range(len(table_values[0])):
			dataline = []
			for j in range(len(table_headers)):
				dataline.append(str(table_values[j][i]))
			table_data.append(dataline)

	elif table_view == 'h':
		table_data = []
		for i in range(len(table_values)):
			table_data.append([table_headers[i]] +
							  list(map(str, table_values[i])))

	table = SingleTable(table_data)
	table.title = table_title
	table.justify_columns = {0: 'left',
							 1: 'left',
							 2: 'left'}
	table.inner_row_border = False
	print(table.table)


def save(value_list, to):
	with open(to, 'w') as f:
		for values in value_list:
		 	print(' '.join(map(str, values)), file=f)

def make_proportional(list1):
	return sum([[str(round(y, 4)), ' '] for y in list1], [])
 	