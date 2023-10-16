def find(n):
    if n==1:
        return 1
    if n<=0:
        return 0
    return find(n-1)+find(n-2)
print(find(4))