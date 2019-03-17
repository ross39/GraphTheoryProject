#Function to match the user input to a given string
#Ross Heaney 

def match(infix, givenString):
	#Use shunting yard algoritm to and convert
	#Expression from infix to postfix
	postfix = infixToPostfix(infix)
	nfa = convertToNFA(givenString)

	#the current set of states and the next set of states
	current = set()
	nexts = set()

	# loop through each character in the string

	for s in givenString:
		
