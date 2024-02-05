'''
*****Linked List - Insert at end & Get name of element at a particular index*****

class Node():
  n = 0
  ptr = None
  head = None

  def __init__(self,name):
    self.i = Node.n
    self.name = name
    self.o = None

  def Insert(self):
    if Node.n == 0:
      Node.head = self
      Node.ptr = self
      Node.n += 1
    elif Node.n == 1:
      Node.head.o = self
      Node.ptr = self
      Node.n += 1
    else:
      Node.ptr.o = self
      Node.ptr = self
      Node.n += 1
  
  def ind(self,n):
    assert n<Node.n
    if self.i == n:
      return self.name
    else:
      return self.o.ind(n)
    

  def display(self,s = ''):
    if self.i == 0:
      s = self.name
    else:
      s = s + ' ' + self.name
    if self.i == Node.n - 1:
      return s
    else:
      return self.o.display(s)
      

num = int(input())
for i in range(num):
  Node.Insert(Node(input()))

linked_list = Node.head

print(linked_list.display())
# print(linked_list.ind(2)) Prints the name of the element in the linked list corresponding
# to the index 'i' mentioned
'''

'''
*****Linked List - Insert at front & Delete from the beginning*****
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#class Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  
  def push_front(self, newElement):
    newNode = Node(newElement)
    newNode.next = self.head 
    self.head = newNode   

  def delete(self,num,cnt=0):
    try:
      if cnt == num:
        return self
      else:
        self.head = self.head.next
        cnt += 1
        return self.delete(num,cnt)
    except:
      return False

  def display(self,s=''):
    if self.head == None:
      return ''
    else:
      if self.head.next == None:
        s = s + ' ' + str(self.head.data)
        return s.strip()
      else:
        s = s + ' ' + str(self.head.data)
        self.head = self.head.next
        return self.display(s)
      
MyList = LinkedList()

MyList.push_front(10)
MyList.push_front(20)
MyList.push_front(30)
MyList.push_front(40)
MyList.push_front(50)
MyList.push_front(60)
MyList.push_front(70)
MyList.push_front(80)
MyList.push_front(90)

#Write your delete code

num = int(input())
DeletedList = MyList.delete(num)
if DeletedList == False:
  print(-1)
else:
  print(DeletedList.display())
'''