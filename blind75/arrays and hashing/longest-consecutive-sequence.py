import numpy as np

from typing import List
class Solution:
    def checkCon(self, a, b):
        if a - b == 1 or a - b == -1:
            return True
        else:
            return False

    def longestList(self, a):
        res = 0
        for i in a:
            if len(i) >= res:
                res = len(i)
        return res

    def longestConsecutive(self, nums: List[int]) -> int:
        temp = []
        nums.sort()
        nums = np.unique(nums)
        alpha = []
        if len(nums) == 1:
            return 1
        else:
            for i in range(len(nums) - 1):
                if len(alpha) == 0:
                    a = nums[i]
                    alpha.append(a)
                elif len(alpha) > 0:
                    a = alpha[-1]
                b = nums[i + 1]
                # print('alpha: ',alpha)
                if self.checkCon(b, a) == True:
                    alpha.append(b)
                else:
                    temp.append(alpha)
                    alpha = [b]

        temp.append(alpha)
        print(temp)
        res = self.longestList(temp)
        print(res)
        return res
