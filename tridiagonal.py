import math
import helper

def tridiagonal(tuples, rs):
	b, c, d = tuples[0]
	g_Deltas = [c]
	g_deltas = [-d / c]
	g_lambdas = [rs[0] / c]
	for i in range(1, len(rs)):
		b, c, d = tuples[i]
		r = rs[i]
		g_Delta = (c + b * g_deltas[i - 1])
		g_delta = -d / g_Delta
		g_lambda = (r - b * g_lambdas[i - 1]) / g_Delta
		g_Deltas.append(g_Delta)
		g_deltas.append(g_delta)
		g_lambdas.append(g_lambda)

	xs = [g_lambdas[-1]]
	for i in range(2, len(rs) + 1):
		xs.append(g_deltas[-i] * xs[i - 2] + g_lambdas[-i])
	xs.reverse()
	
	return xs

if __name__ == '__main__':

	tuples = [
		(0, 2, 1), 
		(2, 9, 2), 
		(4, 17, -4),
		(4, 15, -8), 
		(2, 3, 0)
	]

	rs = [-10, -26, -16, -2, 16]
	xs = tridiagonal(tuples, rs)
	print(xs)




