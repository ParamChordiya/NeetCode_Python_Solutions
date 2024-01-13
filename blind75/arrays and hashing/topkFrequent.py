from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Returns the k most frequent elements in the given list of integers.

        Parameters:
        - nums (List[int]): The input list of integers.
        - k (int): The number of most frequent elements to return.

        Returns:
        - List[int]: A list containing the k most frequent elements.

        Example:
        solution = Solution()
        solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
        [1, 2]
        """
        # Sort the input list
        nums.sort()

        # Count the occurrences of each element
        numsd = {}
        for i in nums:
            if i in numsd:
                numsd[i] += 1
            else:
                numsd[i] = 1

        # Sort elements by their frequency in descending order
        keys = sorted(numsd, key=numsd.get, reverse=True)

        # Select the k most frequent elements
        final = []
        for i in range(k):
            final.append(keys[i])

        return final
