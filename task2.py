import math
import matplotlib.pyplot as plot
import numpy as np
import helper

f = math.sin
xs = np.arange(-3, 3, 0.5)
ys = [f(x) for x in xs]

help_expr = lambda x, xi: np.prod([x - i for i in xs if not xi == i])
l = lambda xi, x: help_expr(x, xi) / help_expr(xi, xi)

def lagrange(x, xs, ys):
	lst = []
	for i in range(len(xs)):
		lst.append(l(xs[i], x) * ys[i])
	return np.sum(lst)

interxs = np.arange(-3, 3, 0.25)
interys = [lagrange(x, xs, ys) for x in interxs]

table_headers = ['x', 'f(x)', 'L(x)']

table_values = [
	interxs[:7],											# x
	helper.make_proportional(ys)[:7],						# f(x)
	list(map(lambda y: round(y, 4), interys))[:7]]			# L(x)

if __name__ == '__main__':

	helper.print_table(
		table_headers,
		table_values,
		table_title='Lagrange',
		table_view='h')

	#plot.plot(xs, ys, "o-")
	#plot.plot(interxs, interys)
	#plot.show()
