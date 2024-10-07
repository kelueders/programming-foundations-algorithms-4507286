# Example file for Programming Foundations: Algorithms by Joe Marini
# try out the Python stack functions

"""
Stack
- collection that supports push and pop operations
- the last item pushed on is the first one popped off
- LIFO = last in, first out
- pushing an item in is constant time operation
- uses:
  - expression processing
  - backtracking - for example, browser back stack

Queue
- collection that supports adding and removing
- FIFO = first in, first out
- uses:
  - order processing - ensures the orders are fullfilled in the order they were received
  - messaging
"""

# TODO: create a new empty stack
stack = []


# TODO: push items onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4) # last one on, first one off


# TODO: print the stack contents
print(stack)


# TODO: pop an item off the stack
x = stack.pop() # pops the first item in
print(x)
print(stack)