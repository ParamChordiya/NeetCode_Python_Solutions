class Solution:
    def binary(self,arr, target):
        l = 0
        r = len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if target == arr[mid]:
                return mid
            elif target < arr[mid]:
                r = mid-1
            elif target > arr[mid]:
                l = mid+1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        # nums=[0,1,2,3,4]
        temp3 = self.binary(nums,target)
        if temp3!=-1:
            return temp3
        else:
            for i in range (len(nums)-1):
                if nums[i+1]<nums[i]:
                    l1 = nums[:i+1]
                    l2 = nums[i+1:]
                    temp = self.binary(l1,target)
                    temp2 = self.binary(l2,target)
                    print(temp)
                    print(temp2)
                    if temp!=-1:
                        return temp
                    elif temp == -1 and temp2!=-1:
                        return temp2+len(l1)
            return -1

        
        
        


        