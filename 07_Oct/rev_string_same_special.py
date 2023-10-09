'''Reverse the given string and keeping its special character at the same place.
Eg:
I/P: srin#ivas
O/P:savi#nirs
I/O:we@lcome
O/P:em@oclem
I/P:pyth#on
O/P:noht#yp'''
s=input()
s=list(s)
m=[]
n=[]
for i in range(len(s)):
    if(s[i].isalnum()):
        m.append(s[i])
    else:
        c=i     
m.reverse()
m.insert(c,s[c])
r = ''.join(map(str, m))
print(r)


        
        
        
    