

import math
import random



def CostFunction(a):
	# y = 2 * sin(2*pi * 4 * x) + 3
	x_set = [0, 1/48, 1/16]
	y_calc = [3, 4, 5]
	y_pso = [a[0] * math.sin(2 * math.pi * a[1] * x) + a[2] for x in x_set]
	err = [abs(yc - yp) for yc, yp in zip(y_calc, y_pso)]
	return  math.fsum(err)


if __name__ == "__main__":

	# config
	pmin = (0.0, 0.0, 0.0)
	pmax = (5.0, 5.0, 5.0)
	pdelta = [1.0, 1.0, 1.0]
	tolerance = 1e-3
	max_iter = 100

	# properties
	ndims = len(pmin)
	pvals = [random.uniform(pi, px) for pi, px in zip(pmin, pmax)]	
	# pvals = [1.0 for _ in pmin]
	best_err = float('inf')

	for itr in range(max_iter):
		for n in range(ndims):
			# calc cost function
			pvals[n] = pvals[n] + pdelta[n]
			err = CostFunction(pvals)

			if err < best_err:
				best_err = err
				pdelta[n] = pdelta[n] * 1.1
			else:
				pvals[n] = pvals[n] - (pdelta[n] * 2)
				err = CostFunction(pvals)

				if err < best_err:
					best_err = err
					pdelta[n] = pdelta[n] * 1.1
				else:
					pvals[n] = pvals[n] + pdelta[n]
					pdelta[n] = pdelta[n] * 0.9
				#endif
			# endif

			print("#{} - e: {:.3f}, p: {:.2f}, {:.2f}, {:.2f}".format(itr, best_err, pvals[0], pvals[1], pvals[2]))
		#endfor
		if best_err < tolerance:
			break
	#endfor


# https://martin-thoma.com/twiddle/
# https://medium.com/intro-to-artificial-intelligence/pid-controller-udacitys-self-driving-car-nanodegree-c4fd15bdc981

