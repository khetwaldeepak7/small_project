for i in range(1,5):
	k=i
	for j in range(1,8):
		if(j>=5-i and j<=3+i):
			if(k>=1 and j>=4):
				print(k,end=" ")
				k=k+1
			else:
				print(k,end=" ")
				k=k-1
		else:
			print(" ",end=" ")
	print( )