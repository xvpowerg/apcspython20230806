class Stack():
    def __init__(self,capacity):
        self.my_stack = [None]*capacity
        self.top = -1
        self.capacity = capacity

    def push(self,data):
        if self.isFull():
            print("滿")
        else:
            self.top += 1
            self.my_stack[self.top] = data
    def pop(self):
        if self.isEmpty():
            print("空")
        else:
           data = self.my_stack[self.top]
           self.my_stack[self.top] = None
           self.top -= 1
           return data
        
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def isFull(self):
        if self.top >= self.capacity - 1:
            return True
        else:
            return False

   
stack = Stack(3)
stack.push("A")
stack.push("B")
stack.push("C")

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
#stack.push("D")


