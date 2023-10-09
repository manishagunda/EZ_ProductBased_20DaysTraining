'''Take the input from the user in the given format(consist of name and code)
find the max digit from the code which is less or equal to the length of string
and put that place char in final string, if there is no any digit found which
not satisfy the condition that simply put 'X'.
#input:
Abhishek:43848,Mayur:3749,Friend:3949,Yeah:7878 #Output:kueX'''

name=[['Abhishek','43848'],['Mayur', '3749'],['Friend','3949'],['Yeah','7878']]
s=''
m=[]
n=[]
o=[]
op=''
for i in name:
    m.append(i[0])
for i in name:
    n.append(i[1])
for i in range(len(m)):
    q=[]
    for p in m[i]:
        q.append(p)
        for j in range(len(n)):
            l=0
            for k in n[j]:
                k=int(k)
                if k<=len(m[i]) and k>l :
                    l=k
            if l==0:
                o.append('x')
                
    o.append(q[l-1])
print(''.join(map(str, o)))      
                    
    
    
        
            
        
        
    
