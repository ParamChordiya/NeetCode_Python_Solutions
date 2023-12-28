from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Determines if the given list of integers contains any duplicates.

        Parameters:
        - nums (List[int]): The input list of integers.

        Returns:
        - bool: True if there are duplicates in the list, False otherwise.

        Example:
        solution = Solution()
        solution.containsDuplicate([1, 2, 3, 4])
        False
        solution.containsDuplicate([1, 2, 3, 1])
        True
        """
        # Count the occurrences of each element
        new_d = {}
        for i in nums:
            if i in new_d:
                new_d[i] += 1
            else:
                new_d[i] = 1

        # Check if there are any elements with more than one occurrence
        flag = False
        for i in new_d.values():
            if i > 1:
                flag = True
                break

        return flag
