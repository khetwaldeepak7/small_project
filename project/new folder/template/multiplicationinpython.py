'''
class A:
	def __init__(self):
		print("hi")
class B(A):   # this is how to inheritage in python
	def m1(self):
		print("bye")
b=B()
'''



a=[10,2,3,4,3,14]
#a.sort()  # direct method to perform sorting
for i in range(len(a)):  # manually i have done the sorting
	for j in range(i+1,len(a)):
		if(a[i]>a[j]):
			temp=a[j]
			a[j]=a[i]
			a[i]=temp
print(a)
