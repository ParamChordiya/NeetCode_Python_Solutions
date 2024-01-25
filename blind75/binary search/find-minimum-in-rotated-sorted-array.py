class Solution:
    def findMin(self, nums: List[int]) -> int:
        # splitVal = nums[0]
        # for i in range(len(nums)-1):
        #     if nums[i+1] < nums[i]:
        #         splitVal = nums[i+1]
        #         s1 = nums[:i+1]
        #         s2 = nums[i+1:]
        # print(splitVal)
        # return splitVal

        left, right = 0,len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right = mid
        return nums[left]

        