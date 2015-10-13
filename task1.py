import math
import helper

VAR = 3
EPS = 1e-5

xs = range(-5, 6)
sums = []
ns = []
for x in xs:
	fx = var * x
	sum = fx
	i = 3
	n = 0
	while math.fabs(fx) > EPS:
		fx *= -((VAR * x) ** 2) / (i * (i - 1))
		sum += fx
		i += 2
		n += 1
	sums.append(round(sum, 4))
	ns.append(n)

helper.print_table(table_headers=['x', 's', 'n'],
				   table_values=[xs, sums, ns],
				   table_title='Lagrange')