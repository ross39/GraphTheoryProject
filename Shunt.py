#import operators
def parse(regex):
    """
    Function to parse infix to postfix using the function 
    yard algorithm
    """
    #convert prefix to postfix . | *
    opStack = ""
    postfix = ""
    print("Please enter query string: ")
    query = input()
    #make dictionary of special chars
    specialChar = {'^':100,'$':0,'*': 90,'+':80,'?':70,'.':60,'|':50}
    #for each character in regular expression
    for i in regex:
        if i == '(':
            opStack = opStack + i
        elif i == ')':
            #check if opStack - 1 == ) if not keep adding stack to pofix then pop items off stack
            while opStack[-1] != '(':
                postfix,opStack = postfix + opStack[-1],opStack[:-1]
            #pop ( off stack
            opStack = opStack[:-1]
        elif i in specialChar:
            #check precedence of operators on stack and pop off if none put 0
            while opStack and specialChar.get(i,0) <= specialChar.get(opStack[-1],0):
                postfix,opStack = postfix + opStack[-1],opStack[:-1]
            opStack = opStack + i
        #add random characters or digits to postfix
        else:
            postfix = postfix + i
    #add the operators from stack to pofix then pop off stack
    while opStack:
        postfix,opStack = postfix + opStack[-1],opStack[:-1]
    print(operators.match(postfix,query))
    return postfix