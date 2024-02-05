class Person():
	def __init__(self,name,dob):
		self.name = name
		self.dob = dob
	def __lt__(self,other):
		if self.dob < other.dob:
			return f'{self.name} is older than {other.name}'
		elif self.dob == other.dob:
			return f'{self.name} is of the same age as {other.name}'
		else:
			return f'{self.name} is younger than {other.name}'

class Matrix():
	def __init__(self,v):
		self.v = v
	def __add__(self,other):
		return [self.v[0]+other.v[0],self.v[1]+other.v[1],self.v[2]+other.v[2]]
			
A = Matrix([1,0,0])
B = Matrix([0,1,0])
print(A+B)	

'''
a = input().split(',')
b = input().split(',')

a_dob = ''.join(a[1].split('/')[::-1])
b_dob = ''.join(b[1].split('/')[::-1])

A = Person(a[0],a_dob)
B = Person(b[0],b_dob)

print(A < B)				
'''				