from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        p1 = [1]*(n+1)
        p2 = [1]*(n+1)
        res = []
        n2 = nums[::-1]
        for i in range(n):
            p1[i+1] = p1[i]*nums[i]
        for j in range (n):
            p2[j+1] = p2[j]*n2[j]

        # p1 = [1] + p1
        # p2 = [1] + p2
        p2 = p2[::-1]
        nums = [1] + nums
        for  i in range(1,n+1):
            res.append(p1[i-1] * p2[i])
            # print(p1[i-1] * p2[i])
        print(p1)
        print(p2)
        return res
                    
