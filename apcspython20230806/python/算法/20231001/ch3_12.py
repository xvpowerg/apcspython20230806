class Node():
    def __init__(self,data = None):
            self.data = data 
            self.next = None
            
class LinkedList():
    def __init__(self):
        self.head = None
    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next
            
    def add(self,item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            return
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = newNode
    def getNode(self,index):
         ptr = self.head
         for i in range(index):
             ptr = ptr.next    
             if ptr == None:
                 break
         return ptr         
         
import random
link = LinkedList()
for i in range(5):
    link.add(random.randint(1,100))

link.print_list()                   
#i = random.randint(0,4)
for i in range(5):
    print('索引%d:%d' %(i, 
      link.getNode(i).data))
