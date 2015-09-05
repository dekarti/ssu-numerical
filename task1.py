import math
import helper

eps = 1e-10
xs = range(-5, 5)
sums = []
ns = []
for x in xs:
	fx = 3 * x
	sum = fx
	i = 3
	n = 0
	while math.fabs(fx) > eps:
		fx *= -(3 * x) ** 2 / (i * (i - 1))
		sum += fx
		i += 2
		n += 1
	sums.append(round(sum, 4))
	ns.append(n)

helper.print_table(xs, sums, ns)