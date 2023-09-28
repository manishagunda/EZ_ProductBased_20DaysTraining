def gen(n):
    t=[]
    for i in range(n):
        r=[]
        for i in range(n):
            r.append(i)
        t.append(r)
    return t
print(gen(10))