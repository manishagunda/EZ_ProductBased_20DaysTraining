def fun(n):
    if n<=2:
        return n
    return fun(n-4)+fun(n-2)
r=fun(16)
print(r)