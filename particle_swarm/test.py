#!/usr/bin/env python3

#	--------------------------------------------------------------------------+
#	
#	Python script to test PSO algorithm
#
#	--------------------------------------------------------------------------+

# global libraries
import matplotlib.pyplot as plt
import math

# own library
from pso import Particle_Parameters, Particle, PSO_Algorithm



#	--------------------------------------------------------------------------+
# 	constants
#	--------------------------------------------------------------------------+


#	--------------------------------------------------------------------------+
#	reference
#	--------------------------------------------------------------------------+

t_sim = [x/100 for x in range(250)]
x_sim = [2 * math.sin(2*math.pi * x) for x in t_sim]

plt.plot(t_sim, x_sim)
plt.grid(True)
plt.show()