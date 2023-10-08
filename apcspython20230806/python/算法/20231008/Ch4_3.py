class Stack():
    def __init__(self):
        self.my_stack = []
    def my_push(self,data):
        self.my_stack.append(data)
    def my_pop(self):     
       return self.my_stack.pop()
    def size(self):
       return  len(self.my_stack)
    def isEmpty(self):
       return self.my_stack == []


stack = Stack()
stack.my_push("Apple")
stack.my_push("Banana")
stack.my_push("Cherry")
stack.my_push("Mango")
#print(stack.my_pop())
while not stack.isEmpty():
    print(stack.my_pop())
