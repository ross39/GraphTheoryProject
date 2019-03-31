#define class state to make state objects
class state:
	label = None
	edge1 = None
	edge2 = None
class nfa:
	start = None
	end = None
	#sets parameters of state obj
	def __init__(self,start,end):
		self.start = start
		self.end = end
def pofixNfa(postfix):
	"""
	1.This function takes in an expression in postfix format 
	2. Constructs a non finite automita
	3. It can handle |, *(klene star), +, ?, . operands
	4. It uses stacks(operandStack) to do this
	"""
	operandStack = []
	for c in postfix:
		if(c == '.'):
			#pop 2 nfas off stack
			nfa2 = operandStack.pop()
			nfa1 = operandStack.pop()
			#make the end of edge 1 the beginnning of nfa 2
			nfa1.end.edge1 = nfa2.start
			#create NFA for concatenate
			newNfa = nfa(nfa1.start,nfa2.end)
			operandStack.append(newNfa)
		elif(c == '|'):
			nfa1 =  operandStack.pop()
			nfa2 = operandStack.pop()
			start = state()
			start.edge1 = nfa1.start
			start.edge2 = nfa2.start
			end = state()
			#if 
			nfa2.end.edge1 = end
			nfa1.end.edge1 = end
			newNfa = nfa(start,end)
			operandStack.append(newNfa)
		elif (c == '*'):
			#pop nfa off stack
			nfa1 = operandStack.pop()
			#empty start and end state
			start = state()
			end = state()
			#set start edges
			start.edge1 = nfa1.start
			start.edge2 = end
			#set end edges
			nfa1.end.edge1 = nfa1.start
			nfa1.end.edge2 = end
			newNfa = nfa(start,end)
			operandStack.append(newNfa)
		#0 or more of preceding element
		elif (c == '+'):
			#pop nfa off stack
			#nfa 2 needs to be first
			nfa2 = operandStack.pop()
			nfa1 = operandStack.pop()
			#empty start and end state
			start = state()
			end = state()
			#set start edges
			start.edge1 = nfa1.start
			start.edge2 = end
			#set end edges
			nfa1.end.edge1 = nfa1.start
			nfa1.end.edge2 = nfa2.start
			nfa2.end.edge1 = end
			newNfa = nfa(start,end)
			operandStack.append(newNfa)
		#one or zero
		elif (c == '?'):
			#pop nfa off stack
			#nfa 2 needs to be first
			nfa1 = operandStack.pop()
			#empty start and end state
			start = state()
			end = state()
			#set start edges
			start.edge1 = nfa1.start
			start.edge2 = end
			#set end edges
			nfa1.end.edge1 = end
			newNfa = nfa(start,end)
			operandStack.append(newNfa)
		#starts with Operator
		#needs work
		elif(c == '^'):
			nfa1 = operandStack.pop()
			start = state()
			end = state()
			start.edge1 = nfa1.start
			nfa1.end.edge1 = end
			newNfa = nfa(start,end)
			operandStack.append(newNfa)
		#end operator
		elif(c == '$'):
			nfa1 = operandStack.pop()
			nfa2 = operandStack.pop()
			start = state()
			end = nfa1.start
			start.edge1 = nfa2.start
			nfa2.end.edge1 = nfa1.start
			nfa1.end.edge1 = nfa1.start
			nfa1.end.edge2 = nfa2.start
			newNfa = nfa(start,end)
			operandStack.append(newNfa)
		#else it's characters to perform operations on
		else:
			#create empty start and end states
			end = state()
			start = state()
			#put characters from postfix on label to match
			start.label = c
			start.edge1 = end
			newNfa = nfa(start,end)
			operandStack.append(newNfa)
	return operandStack.pop()
def followEmpty(state):
	states = set()
	states.add(state)
	if state.label is None:
		if state.edge1 is not None:
			states |= followEmpty(state.edge1)
		if state.edge2 is not None:
			states |= followEmpty(state.edge2)
	return states
#takes postfix and query + compares
def match(postfix,query):	
	nfa = pofixNfa(postfix)
	current = set()
	next = set()
	current |= followEmpty(nfa.start)
	for s in query: 
		for c in current:
			if(c.label == s):
				next |= followEmpty(c.edge1)
		current = next
		next = set()
	return(nfa.end in current)

#Here is some test data 
infixes = ["a*","(ab+)c", "aab.bc"]
strings = []
for i in infixes:
	for s in strings:
		print(match(i,s),i,s)