import math
import numpy as np
import matplotlib.pyplot as plot
import helper

from functools import reduce

def divided_differences(xs, ys):
	differences_table = [ys]
	counter = len(xs)
	for i in range(len(xs)):
		differences = []
		for j in range(counter - 1):
			value = (differences_table[i][j] - 		\
					 differences_table[i][j + 1]) / \
					(xs[j] - xs[i+j+1])
			differences.append(value)
		counter -= 1
		differences_table.append(differences)
	return  differences_table[:-1]

def newton(x, xs, ys):
	diff_table = divided_differences(xs, ys)
	result = diff_table[0][0]
	omega = 1
	for i in range(1, len(xs)):
		omega *= (x - xs[i-1])
		result += diff_table[i][0] * omega

	return result

if __name__ == '__main__':
	
	xs = [0.0, 0.2, 0.5, 0.9, 1.4, 2.0, 2.7, 4.0]
	ys = [0.5403, 0.6831, 0.8216, 0.9185, 0.9697, 0.9909, 0.9977, 0.9998]

	#----------------Defining Table of Divided Differences---------------
	table_headers = ['x_i', 'y_i']
	table_values = [xs, ys]

	helper.print_table(
		table_headers,
		table_values,
		table_title='Newton',
		table_view='v')
