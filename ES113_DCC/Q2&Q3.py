class Node():
    head = None
    tail  = None
    cnt = 0

    def __init__(self,data):
        self.data = data
        self.o = None
    
    def addNode(data):
        N = Node(data)
        if Node.cnt == 0:
            Node.head = N
        else:
            Node.tail.o = N
        Node.tail = N
        N.o = None
        Node.cnt+=1
    
    def display():
        i = 1
        t = Node.head
        while t != None:
            print(f'{i}:{t.data} -> ', end='')
            t = t.o
            i+=1
        print('None')
    
    def deleteNodeFromHead(k):
        i = 1
        t = Node.head
        while i < k-1:
            t = t.o
            i+=1
        t.o = t.o.o
    def deleteNodeFromTail(k):
        i = 1
        t = Node.head
        k = Node.cnt-k
        while i < k-1:
            t = t.o
            i+=1
        t.o = t.o.o
    

Node.addNode('Hrriday')
Node.display()
Node.addNode('Debojit')
Node.display()
Node.addNode('Astitva')
Node.addNode('Abhijit')
Node.addNode('Hardik')
Node.display()
Node.deleteNodeFromHead(4)
Node.deleteNodeFromTail(2)
Node.display()
