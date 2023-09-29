n=int(input("enter term"))
n1=0
n2=1
if(n<0):
    print("not possible")
else:
    for i in range(1,n-1):
        n3=n1+n2
        n1=n2
        n2=n3
    print(n,"th term",n3)