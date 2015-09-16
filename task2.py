import math
import helper
import matplotlib.pyplot as plot
import numpy as np

f = math.sin
xs = np.arange(-15, 15, 0.5)
ys = [f(x) for x in xs]

help_expr = lambda x, xi: np.prod([x - i for i in xs if not xi == i])
l = lambda xi, x: help_expr(x, xi) / help_expr(xi, xi)
lagrange = lambda x: np.sum([l(xs[i], x) * ys[i] for i in range(0, len(xs))])

interxs = np.arange(-15, 15, 0.25)
interys = [lagrange(x) for x in interxs]
plot.plot(xs, ys)
plot.plot(interxs, interys)
plot.show()
