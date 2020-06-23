#!/usr/bin/env python3

#	--------------------------------------------------------------------------+
#	
#	Python script to test PSO algorithm
#
#	References
#	* https://medium.com/swlh/inspyred-solving-optimization-problems-with-python-edea4ff7c72b
#
#	--------------------------------------------------------------------------+

# global libraries
import numpy as np
import matplotlib.pyplot as plt
import math

# own library
# from pso import Particle_Parameters, Particle, Algorithm
import pso



#	--------------------------------------------------------------------------+
# 	constants
#	--------------------------------------------------------------------------+


#	--------------------------------------------------------------------------+
#	reference
#	--------------------------------------------------------------------------+

# t_sim = np.arange(0, 2, 10e-3)
# x_sim = 2 * np.sin(2*np.pi * t_sim)

# plt.plot(t_sim, x_sim)
# plt.grid(True)
# plt.show()

#	--------------------------------------------------------------------------+
#	class tester
#	--------------------------------------------------------------------------+

single_param = pso.Particle_Parameters()
single_param.velocity = 10
single_param.position = 5
single_param.coeffs = [3, 9]

print("Params: -> {}".format(single_param))