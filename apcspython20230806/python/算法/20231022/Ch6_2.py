class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end='->')
        if self.right:
            self.right.inorder()

nodeA = Node(14)
nodeB = Node(3) ;  nodeA.left  = nodeB
nodeC = Node(16);  nodeB.left  = nodeC
nodeD = Node(23);  nodeB.right = nodeD
nodeE = Node(7) ;  nodeA.right = nodeE
nodeF = Node(20);  nodeE.right = nodeF

root = nodeA

root.inorder()
