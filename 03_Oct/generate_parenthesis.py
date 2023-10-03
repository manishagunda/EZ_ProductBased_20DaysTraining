def generate(n):
    def g(partial, left, right, valid_combinations=[]):
        if left>0:
            g(partial + '(', left-1,right)
        if right>left:
            g(partial + ')',left,right-1)
        if left==0 and right==0:
            valid_combinations.append(partial)
            return valid_combinations
        return g('',n,n)
n=3
result=generate(n)
print(result)