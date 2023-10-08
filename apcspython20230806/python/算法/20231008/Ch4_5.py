class Queue():
    def __init__(self):
        self.my_queue = []
    def enqueue(self,data):
        self.my_queue.append(data)
    def dequeue(self):    
       return self.my_queue.pop(0)
    def isEmpty(self):     
       return self.my_queue == []

queue = Queue()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

