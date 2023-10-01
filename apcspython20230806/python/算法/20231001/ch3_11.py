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

myList = LinkedList()
myList.add(5)
myList.add(15)
myList.add(25)
myList.print_list()
