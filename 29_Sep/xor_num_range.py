l=int(input("enter lower range"))
n=int(input("enter higher range"))
'''l=2 h=4
   0010
   0011
   0001
   0100
   0101=5'''
if n%4==0:
    a=n
elif n%4==1:
    a=1
elif n%4==2:
    a=n+1
elif n%4==3:
    a=0
if (l-1)%4==0:
    b=n
elif (l-1)%4==1:
    b=1
elif (l-1)%4==2:
    b=n+1
elif (l-1)%4==3:
    b=0
print(a^b)



