n=int(input("enter num"))
k=int(input("enter bit to check"))
a=n&(1<<(k-1))
if a==0:
    print("not set")
else:
    print("set")