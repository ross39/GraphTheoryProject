#goal here is to construct nfa's from the regular expressions

def convertToNFA(postFixExp):
    #build a stack to store stuff
    s=[];stack=[];start=0;end=1
    