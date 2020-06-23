#	--------------------------------------------------------------------------+
#
#	Particle Swarm Optimization
#
#	Heuristic method to find the best solution without detailed knowledge of the 
#	problem being optimized
#
#	Some references
#	* https://en.wikipedia.org/wiki/Particle_swarm_optimization
# 	* https://nathanrooy.github.io/posts/2016-08-17/simple-particle-swarm-optimization-with-python/
#
#	--------------------------------------------------------------------------+


#	--------------------------------------------------------------------------+
#
#	Particle Parameters
#
#	"struct" to store particle values
#
#	--------------------------------------------------------------------------+

class Particle_Parameters():
	def __init__(self):
		self._pos = 0
		self._vel = 0
		self._coefs = []


	def __str__(self):
		return "Position: {}\r\nVelocity: {}\r\nCoefficients: {}\r\n".format(
			self._pos,
			self._vel,
			self._coefs
		)


	@property
	def position(self):
		return self._pos


	@position.setter
	def position(self, val):
		self._pos = val


	@property
	def velocity(self):
		return self._vel


	@velocity.setter
	def velocity(self, val):
		self._vel = val


	@property
	def coeffs(self):
		return self._coefs

	@coeffs.setter
	def coeffs(self, vals):
		self._coefs = vals


#	--------------------------------------------------------------------------+
#
#	Particle class
#
#	
class Particle():
	def __init__(self, randomize = False):
		self._params = Particle_Parameters()


class Algorithm():
	def __init__(self):
		pass


