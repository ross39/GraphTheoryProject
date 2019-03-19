#Function to match the user input to a given string
#Ross Heaney 

def follows(state):
	"""Returns the set of states that can be reached from x """
	states = set()
	set.add(state)

	#check if state has arrows leading from it
	if state.label is None:
		if state.edge1 is not None:
			states |= follows(state.edge1)
		if state.edge2 is not None:
			states |= follows(state.edge2)

	return states

def match(infix, givenString):
	#Use shunting yard algoritm to and convert
	#Expression from infix to postfix
	postfix = infixToPostfix(infix)
	nfa = convertToNFA(givenString)

	#the current set of states and the next set of states
	current = set()
	nexts = set()
	
	#Add initial state to the current state
	current |= follows(nfa.initial)

	# loop through each character in the string

	for s in givenString:
		for c in current:
			if c.label == s:
				next |= follows(c.edge1)

		current = next
		next = set()

	return (nfa.accept in current)

#Some tests
infixes = ["a.b.c", "a.(b|d).c*"]
strings = ["", "abc", "abcc"]

for i in infixes:
	for s in strings:
		print(match(i, s), i, s)

