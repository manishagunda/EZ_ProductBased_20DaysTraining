def find(a,n):
    r=a[0]
    for i in range(1,n):
        r=r^a[i]
    return r
a=[2,3,5,4,5,3,4,2,88]
print(find(a,len(a)))