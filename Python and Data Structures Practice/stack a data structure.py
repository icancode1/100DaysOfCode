from pythonds.basic import Stack

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def secpeek(self):
        if not self.is_empty():
            return self.items[-2]
        
    def get_stack(self):
        return self.items
    
    def check_specific(self):
        if 'maza' in self.items:
            return True
        else:
             return 'Fuck off'
        


s = Stack()
s.push('true')
s.push('hello')
s.push('There')
s.push('Are')
print(s.secpeek())
print(s.get_stack())
print(s.check_specific())
