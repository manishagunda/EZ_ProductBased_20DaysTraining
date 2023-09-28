a=int(input("size"))
l=int(input("lower range"))
h=int(input("higher range"))
k =[]
s =[]
e =[]
print("enter elements")
for i in range(0,a):
    d=int(input())
    if(d>=l and d <= h ) : #(or) if(d>-min(b)
        k.append(d)
    else:
        continue
for i in k:
    if i% 2 ==0 :
        s.append(i)

for i in k:
    for j in range(0,max(s)):
        if (2**j==i) :
            e.append(i)
print(k)
print(s)
print(e)