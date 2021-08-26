from collections import deque

class Stack(deque):
    
    def __init__(self):
        pass

    def push(self, data, e):
        return data.append(e)
    
    def pop(self, data):
        return data.pop()
    
     
myDeque = deque(['One', 'Two', 'Three', 'Four', 'Five'])

myStack = Stack()

myStack.push(myDeque, 'Six')

print(myDeque)

myStack.pop(myDeque)

print(myDeque)
