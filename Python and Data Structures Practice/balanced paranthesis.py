'''
A balanced parenthisis: which has the same opening and 
closing bracket in the nth position and (len-n)th position

eg: ([])
Using stack() in python
'''
from pyarabic.stack import Stack

def balanced_string(balstr):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(balstr) and is_balanced:
        brac = balstr[index]
        if brac in "({['":
            s.push(brac)
        
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top,brac):
                    is_balanced = False

        index= index+1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

def is_match(n1,n2):
    if n1 == "{" and n2 == "}":
        return True
    elif n1 == "[" and n2 == "]":
        return True
    elif n1 == "(" and n2 == ")":
        return True
    else:
        return False
    
print(balanced_string('[{(((([[{{}}]]))))}]'))