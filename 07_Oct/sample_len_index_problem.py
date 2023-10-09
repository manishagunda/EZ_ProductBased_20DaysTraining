'''Take the input from the user in the given format(consist of name and code)
find the max digit from the code which is less or equal to the length of string
and put that place char in final string, if there is no any digit found which
not satisfy the condition that simply put 'X'.
#input:
Abhishek:43848,Mayur:3749,Friend:3949,Yeah:7878 #Output:kueX'''
s=input()
los=s.split(',')
op=''
for i in los:
    nc=i.split(':')
    name=nc[0]
    code=nc[1]
    print(name,code)
    max=0
    for i in code:
        if int(i)>max and int(i)<=len(name):
            max=int(i)
    if max==0:
        op+='x'
    else:
        op+=name[max-1]
print(op)
