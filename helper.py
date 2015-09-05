def print_table(xs, res, ns):
	print (' x |', end='')
	for x in map(str, xs):
		print(x.rjust(10), '|', end='')

	print('\n', 's |', end='')
	for r in map(str, res):
		print(r.rjust(10), '|', end='')

	print('\n', 'n |', end='')
	for n in map(str, ns):
		print(n.rjust(10), '|', end='')

	print('\n')

	