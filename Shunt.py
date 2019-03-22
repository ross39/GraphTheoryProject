#Shunting yard algorithm
#Ross Heaney
#Reads in infix expression and converts to postfix

class ConvertToPostfix:

    #Here we have a constructor
    #self.precedence means that we set the precedence for the operands. Higer == more important
    def __init__(self, capacity): 
        self.top = -1 
        self.capacity = capacity 
        # This array is used a stack  
        self.array = [] 
        # Precedence setting 
        self.output = [] 
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3} 

    # check if the stack is empty 
    def isEmpty(self): 
        return True if self.top == -1 else False
      
    # Return the value of the top of the stack 
    def peek(self): 
        return self.array[-1] 

    # Pop the element from the stack 
    def pop(self): 
        if not self.isEmpty(): 
            self.top -= 1
            return self.array.pop() 
        else: 
            return "$"
    # Push the element to the stack 
    def push(self, op): 
        self.top += 1
        self.array.append(op)  
    
    # A utility function to check is the given character 
    # is operand  
    def isOperand(self, ch): 
        return ch.isalpha() 
  
    # Check if the precedence of operator is strictly 
    # less than top of stack or not 
    def notGreater(self, i): 
        try: 
            a = self.precedence[i] 
            b = self.precedence[self.peek()] 
            return True if a  <= b else False
        except KeyError:  
            return False
    
    #Here we have the meat of the program. 
    def infixToPostfix(self, infixExp):
        for i in infixExp:
            # If the character is an operand,  
            # add it to output 
            if self.isOperand(i): 
                self.output.append(i) 
            # If the character is an '(', push it to stack 
            elif i  == '(': 
                self.push(i) 
            # If the scanned character is an ')', pop and  
            # output from the stack until and '(' is found 
            elif i == ')': 
                while( (not self.isEmpty()) and self.peek() != '('): 
                    a = self.pop() 
                    self.output.append(a) 
                if (not self.isEmpty() and self.peek() != '('): 
                    return -1
                else: 
                    self.pop() 
            
             # An operator is encountered 
            else: 
                while(not self.isEmpty() and self.notGreater(i)): 
                    self.output.append(self.pop()) 
                self.push(i) 

         # pop all the operator from the stack 
        while not self.isEmpty(): 
            self.output.append(self.pop()) 
  
        print ("".join(self.output))        
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = ConvertToPostfix(len(exp)) 
obj.infixToPostfix(exp) 