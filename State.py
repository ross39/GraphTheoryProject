#create a class to store the state of the NFA

class State:
    def __init__(self, name):
        self.epsilon = [] # epsilon-closure
        self.transitions = {} # a dictionary of char --> state
        self.name = name
        self.is_end = False # is it the ending state?