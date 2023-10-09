'''input: A string of comma separated numbers are given such that the
numbers 4 and 7 are already available in the list. Assumption:7 always
comes after 4 in the given string. Number1=Add all numbers which do not lie
b/w 4 and 7(excluding4 and 7) in the given input.
Number2:numbers formed by cancatinating all numbers from 4 to 7
(including 4 n 7)
0/p: sum of Number1 and Number2
Example: 2,5,1,4,3,2,7,8
Number1:2+5+1+8=16
Number2: '4'+'3'+'2'+'7'='4327'
o/p:16+4327=4343'''
s=input()
s=s.split(",")
d=s.index('4')
c=s.index('7')
m=''
k=0
for i in range(len(s)):
    if i>=d and i<=c:
        m=m+s[i]
    else:
        k=k+int(s[i])
print(int(m)+k)

        
    
        
        
        
        


