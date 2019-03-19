#goal here is to construct nfa's from the postfix expression

def post2nfa(postre):
    '''Create a NFA from a postfix regular expression'''

    myStack = []
    class state:
        def __init__(self,c):
            self.c = c
            self.out = None
            self.out1 = None
            #for patch, if state is a split then join out1 with new state 
            #otherwise join out.

    class frag:
        '''A "fragment" of computation'''

        def __init__(self,start,dangling_states):
            self.start = start
            self.out = dangling_states
            #out is a list of states with dangling arrows.

    for c in postre:
        if c == '.':
            f2 = myStack.pop()
            f1 = myStack.pop()
            patch(f1.out,f2.start)
            f1.out = f2.out
            myStack.append(f1)
        
        elif c == '?':
            f = myStack.pop()
            someState = state(-1)
            someState.out = f.start
            f.out.append(someState)
            f.start = someState
            myStack.append(f)

        elif c == '*':
            f = myStack.pop()
            otherState = state(-1)
            otherState.out = f.start
            patch(f.out,otherState)
            f.out = [otherState]
            f.start = otherState
            myStack.append(f)

        elif c == '+':
            f = myStack.pop()
            ormstate = state(-1)
            ormstate.out = f.start
            patch(f.out,ormstate)
            f.out = [ormstate]
            myStack.append(f)
            
        elif c == '|':
            f2 = myStack.pop()
            f1 = myStack.pop()
            orstate = state(-1)
            orstate.out = f2.start
            orstate.out1 = f1.start
            f1.start = orstate
            f1.out = f1.out + f2.out
            myStack.append(f1)

        else:
            atom_state = state(c)
            f = frag(atom_state,[atom_state])
            myStack.append(f)

    if myStack: 
        f = myStack.pop()
        patch(f.out, state(-2))
        return f.start
    return state(-2)