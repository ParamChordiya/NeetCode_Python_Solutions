from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the indices of two numbers in the given list that add up to the target.

        Parameters:
        - nums (List[int]): The input list of integers.
        - target (int): The target sum to be achieved.

        Returns:
        - List[int]: A list containing the indices of the two numbers that add up to the target.

        Example:
        solution = Solution()
        solution.twoSum([2, 7, 11, 15], 9)
        [0, 1]
        solution.twoSum([3, 2, 4], 6)
        [1, 2]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Check if the sum of two numbers equals the target
                if nums[i] + nums[j] == target:
                    return [i, j]
