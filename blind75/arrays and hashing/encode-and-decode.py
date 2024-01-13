class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        s=""
        for i in strs:
            s=s+i+"::;"
        print(s)
        return s

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        x = str.split("::;")
        print(x)
        return x