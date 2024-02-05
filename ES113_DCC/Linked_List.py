class Node():
	def __init__(self,data):
		self.data = data
		self.next = None
	
class Linked_List():
	head = None
	tail = None
	n = 0
	def Insert_At_End(data):
		node = Node(data)
		if Linked_List.n == 0:
			Linked_List.head = node
			Linked_List.tail = node
			Linked_List.n += 1
		else:
			Linked_List.tail.next = node
			Linked_List.tail = node
			Linked_List.n += 1
	def Display():
		a = Linked_List.head
		s = ''
		for i in range(Linked_List.n):
			s = s + f'{a.data}' + ' -> '
			a = a.next
		s += 'None'
		return s			
	def Del_From_Beg():
		a = Linked_List.head.next
		Linked_List.head = a
		Linked_List.n -= 1
		return Linked_List.Display()
	def Del_k(k):
		if k>Linked_List.n:
			return 'Not Possible'
		elif k == 1:
			Linked_List.Del_From_Beg()
		else:
			a = Linked_List.head
			for i in range(2,k):
				a = a.next
			a.next = a.next.next
			Linked_List.n -= 1
		return Linked_List.Display()
ll = Linked_List
ll.Insert_At_End(10)
ll.Insert_At_End(20)
ll.Insert_At_End(30)
ll.Insert_At_End(40)
print(ll.Display())
print(ll.Del_From_Beg())
print(Linked_List.n)
print(ll.Del_k(4))
	
				