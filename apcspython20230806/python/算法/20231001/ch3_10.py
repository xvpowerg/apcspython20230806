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
            
link = LinkedList()
n1 = Node(5)
n2 = Node(15)
n3 = Node(25)
link.head = n1
link.head.next = n2
n2.next = n3

link.print_list()





