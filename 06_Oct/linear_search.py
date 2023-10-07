def linear_search(l,e):
    flag=0
    for i in range(len(l)):
        if l[i]==e:
            return i
    return 0
l=list(map(int,input().split()))
e=int(input("enter element"))
res=linear_search(l,e)
if res!=0:
    print("element found at",res)
else:
    print("element not found")
