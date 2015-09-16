import math
import helper

var = 3
eps = 1e-5
xs = range(-5, 6)
sums = []
ns = []
for x in xs:
	fx = var * x
	sum = fx
	i = 3
	n = 0
	while math.fabs(fx) > eps:
		fx *= -((var * x) ** 2) / (i * (i - 1))
		sum += fx
		i += 2
		n += 1
	sums.append(round(sum, 4))
	ns.append(n)

helper.print_table(xs, sums, ns)