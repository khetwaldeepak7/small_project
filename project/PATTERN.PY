# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

#print("Hello world")
'''
for i in range(1,6):
    k=i
    t=4
    for j in range(1,6):
        if(i>=j):
            print(k,end=" ")
            k=k+t
            t=t-1
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
   # print("##")
  '''
k=1
for i in range(1,6):
   for j in range(1,6):
       if(i>=j):
          print(k,end=" ")
          k=k+1
       else:
          print(" ",end=" ")
    
   print( )