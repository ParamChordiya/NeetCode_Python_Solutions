class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines if two input strings are anagrams of each other.

        An anagram is a word or phrase formed by rearranging the letters of
        another. For the purpose of this function, two strings are considered
        anagrams if they have the same characters with the same frequency.

        Parameters:
        - s (str): The first input string.
        - t (str): The second input string.

        Returns:
        - bool: True if the strings are anagrams, False otherwise.

        Example:
        solution = Solution()
        solution.isAnagram("listen", "silent")
        True
        solution.isAnagram("hello", "world")
        False
        """
        # Initialize dictionaries to store character frequencies
        s_dict = {}
        t_dict = {}

        # Check if the lengths of the two strings are equal
        if len(s) != len(t):
            return False
        else:
            # Count the occurrences of each character in the first string
            for i in range(len(s)):
                if s[i] in s_dict:
                    s_dict[s[i]] += 1
                else:
                    s_dict[s[i]] = 1

            # Count the occurrences of each character in the second string
            for i in range(len(s)):
                if t[i] in t_dict:
                    t_dict[t[i]] += 1
                else:
                    t_dict[t[i]] = 1

            # Compare the character frequencies of the two strings
            if s_dict == t_dict:
                return True
