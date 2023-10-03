'''Write a Python Function min_moves_to_solve_hanoi(n) that calculates and returns the minimum
number of moves required to solve the Tower of Hanoi puzzle for n disks.
Sample Input 3
Sample Output 7'''
def TOH(n,src,aux,dest):
    if n==1:
        print(" I moved from " +src+ " to " +dest)
        return
    TOH(n-1,src,dest,aux)
    print(" I moved from " +src+ " to " +dest)
    TOH(n-1,aux,src,dest)
n=2
TOH(n,'src','aux','dest')