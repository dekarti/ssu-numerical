import math
import matplotlib.pyplot as plot
import helper

from functools import reduce

xs = list(helper.frange(-3, 3, 0.5))
ys = [math.sin(x) for x in xs]

def help_expr(x, xi):
	lst = [x - i for i in xs if not xi == i]
	return reduce(lambda res, x: res * x, lst, 1)

def L(xi, x):
	return help_expr(x, xi) / help_expr(xi, xi)

def lagrange(x, xs, ys):
	lst = []
	for i in range(len(xs)):
		lst.append(L(xs[i], x) * ys[i])
	return sum(lst)

if __name__ == '__main__':

	interxs = list(helper.frange(-3, 3, 0.25))
	interys = [lagrange(x, xs, ys) for x in interxs]

	table_headers = ['x', 'f(x)', 'L(x)']

	table_values = [
		interxs,										# x
		helper.make_proportional(ys),					# f(x)
		list(map(lambda y: round(y, 4), interys))]		# L(x)

	helper.print_table(
		table_headers,
		table_values,
		table_title='Lagrange',
		table_view='v')

	#plot.plot(xs, ys, "o-")
	#plot.plot(interxs, interys)
	#plot.show()
