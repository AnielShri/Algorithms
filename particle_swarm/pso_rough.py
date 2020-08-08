


import random
import math


class Particle(object):
	def __init__(self):
		self._index = None
		self._position = []
		self._velocity = None
		self._best_err = float('inf')
		self._best_pos = []

	def __str__(self):
		str_p = ["{:.2f}".format(p) for p in self._best_pos]
		return "#{} - err: {:.3f}, pos: {}".format(self._index, self._best_err, ', '.join(str_p))


def CostFunction(a):
	# y = 2 * sin(2*pi * 4 * x) + 3
	x_set = [0, 1/48, 1/16]
	y_calc = [3, 4, 5]
	y_pso = [a[0] * math.sin(2 * math.pi * a[1] * x) + a[2] for x in x_set]
	err = [abs(yc - yp) for yc, yp in zip(y_calc, y_pso)]
	return  math.fsum(err)


if __name__ == "__main__":
	# config
	pmin = (0, 0, 0)
	pmax = (5, 5, 5)
	initial = (1, 1, 1)
	ndims = len(pmin)
	npart = 40
	niter = 500

	w = 0.5      	# constant inertia weight; lower = fater; higher = explores more of search space
	c1 = 1.8        # cognative constant
	c2 = 1.9        # social constant

	# variables
	_swarm = []
	_gbest_err = float('inf')
	_gbest_pos = []

	# init
	for n in range(npart):
		_swarm.append(Particle())
		_swarm[n]._index = n
		_swarm[n]._position = [random.uniform(minpos, maxpos) for minpos, maxpos in zip(pmin, pmax)]
		# _swarm[n]._position = [1 for _ in pmin]
		_swarm[n]._velocity = [random.uniform(-1, 1) for _ in pmin]

	for itr in range(niter):
	# calc costfunc
		for p in _swarm:
			err = CostFunction(p._position)
			if err < p._best_err:
				p._best_err = err
				p._best_pos = p._position.copy()
			if err < _gbest_err:
				_gbest_err = err
				_gbest_pos = p._position.copy()

			# print(p)
		print("#{} - err: {:.2f}, pos: {}".format(
			itr,
			_gbest_err, 
			["{:.2f}".format(gb) for gb in _gbest_pos])
			)

		# calc new velocity
		for p in _swarm:
			for n in range(ndims):
				vel_inertia = w * p._velocity[n]
				vel_cognitive = c1 * random.random() * (p._best_pos[n] - p._position[n])
				vel_social = c2 * random.random() * (_gbest_pos[n] - p._position[n])
				p._velocity[n] = vel_inertia + vel_cognitive + vel_social

		# calc new position
		for p in _swarm:
			for n in range(ndims):
				pos = p._position[n] + p._velocity[n]
				if pos > pmax[n]:
					pos = pmax[n]
				if pos < pmin[n]:
					pos = pmin[n]
				p._position[n] = pos

		if err < 1e-3:
			break # good enough?



		

