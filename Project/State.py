#create a class to store the state of the NFA
#Ross Heaney

class State:
	label1 = None
	edge1 = None 
	edge2 = None

class Nfa:
	initial = None
	accept = None

	def __init__(self, initial, accept):
		self.initial = initial
		self.accept = accept
