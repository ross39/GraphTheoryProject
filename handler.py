#This handles all the hard stuff

class state:
    label = None
    edge1 = None 
    edge2 = None

#An NFA is represented by it's initial and accepts
class nfa:
    initial = None 
    accept = None


    def__init__(self, initial, accept):
    self.initial = initial
    self.accept = accept
    
def construct(postfix):
    nfastack = []
    for c in postfix:
        if c == '.':
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()

            nfa1.accept.edge1 = nfa2.initial
            nfastack.append(nfa1.initial, nfa2.accept))

        elif c == '|':
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            