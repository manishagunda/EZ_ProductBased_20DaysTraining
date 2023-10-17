# 238. product-of-array-except-self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
    
        left_product = 1
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]
    
  
        right_product = 1
        for i in range(n - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]
    
   
        answer = [left_products[i] * right_products[i] for i in range(n)]
        
        return answer
    
#239. sliding-window-maximum
class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        window = deque()

        for i, num in enumerate(nums):
            while window and window[0] < i - k + 1:
                window.popleft()

            while window and nums[window[-1]] < num:
                window.pop()

            window.append(i)

            if i >= k - 1:
                result.append(nums[window[0]])

        return result
# 234. palindrome-linked-list
lass Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        temp=head
        while temp is not None:
            stack.append(temp.val)
            temp=temp.next
        stack=stack[::-1]
        i=0
        temp=head
        while temp is not None:
            if temp.val !=stack[i]:
                return False
            temp=temp.next
            i+=1
        return True
#233. number-of-digit-one
class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1
        while factor <= n:
            divider = factor * 10
            count += (n // divider) * factor + min(max(n % divider - factor + 1, 0), factor)
            factor *= 10
        return count
#231. power-of-two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        return(n & n-1)==0
#229. majority-element-ii
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_map={}
        ans=[]
        for e in nums:
            if e not in my_map:
                my_map[e]=1
            else:
                my_map[e]=my_map[e]+1
        n=len(nums)/3
        for key in my_map:
            if my_map[key]>n:
                ans.append(key)
        return ans
#219. contains-duplicate-ii
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_map={}
        for i in range(len(nums)):
            key=nums[i]
            value=i
            if key in my_map:
                j=my_map[key]
                if abs(value-j)<=k:
                    return True
            my_map[key]=value
        return False
# 