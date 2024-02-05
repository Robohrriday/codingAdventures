class Node():
    head = None
    tail  = None
    cnt = 0

    def __init__(self,data):
        self.data = data
        self.o = None
        self.i = None
    
    def addNode(data):
        N = Node(data)
        if Node.cnt == 0:
            Node.head = N
        else:
            Node.tail.o = N
            N.i = Node.tail
        Node.tail = N
        N.o = None
        Node.cnt+=1
    
    def display():
        t = Node.head
        while t != None:
            print(f'{t.data} -> ', end='')
            t = t.o
        print('None')
    
    def index(num):
        cnt = 0
        t = Node.head
        while cnt < num:
            t = t.o
            cnt += 1
        return t.data
    
    def insertionSort():
        t = Node.head
        while t.o != None:
            if t.data>t.o.data:
                t.data,t.o.data = t.o.data,t.data
                if t.i != None:
                    t = t.i 
            else:
                t = t.o
    
    def bubbleSort():
        i = 0
        while i < Node.cnt-1:
            t = Node.head
            while t.o!=None:
                if t.data>t.o.data:
                    t.data,t.o.data=t.o.data,t.data
                t = t.o
            i+=1

Node.addNode(1)
Node.addNode(-1)
Node.addNode(10)
Node.addNode(4)
Node.addNode(9)
Node.addNode(6)
Node.insertionSort()
print()
Node.display()