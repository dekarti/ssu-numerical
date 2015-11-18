import newton
import helper
import tridiagonal


def build_tuples(xs, ys):
	hs = [xs[k] - xs[k-1] for k in range(1, len(xs))]
	dd = newton.divided_differences(xs, ys)[1]
	tuples = []
	rs = []
	for k in range(1, len(hs)):
		tuples.append((
				hs[k - 1],
				2 * (hs[k - 1] + hs[k]),
				hs[k]
		))
		rs.append(3 * (dd[k] - dd[k - 1]))

	return (tuples, rs)

def spline(xs, ys):
	tuples, rs = build_tuples(xs, ys)
	cs = [0] + tridiagonal.tridiagonal(tuples, rs) + [0]
	print(cs)





if __name__ == '__main__':

	#xs = range(1, 7)
	#ys = [1.0002, 1.0341, 0.6, 0.40105, 0.1, 0.23975]
	xs = [-1, 0, 3]
	ys = [0.5, 0, 3]

	spline(xs, ys)