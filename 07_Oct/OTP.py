'''Input: 7564168
Separate odd integers: 5,4,6, return 4 digit OTP by squaring the digits
Digits from above 5,4,6
Squares are 25,16,36
return 2516 as OTP'''
#1
n=(input())
n=list(n)
m=[]
for i in range(0,len(n)):
    if i%2!=0:
        n[i]=(int(n[i])**2)
        m.append(n[i])
r = ''.join(map(str, m))
print(int(str(r)[:4]))
#2
n=input()
s=""
for i in range(1,len(n),2):
    s=s+str(int(n[i])**2)
print(s[:4])
#3
def demo(n):
    n=str(n)
    s=""
    for i in range(1,len(n),2):
        s=s+str(int(n[i])**2)
        s=s[:4]
    return s
if __name__=='__main__':
    print(demo(7564168))

    

        
    

        