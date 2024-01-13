class Solution:
    def getReverse(self,s):
        l = list(s)
        l=l[::-1]
        res =""
        for i in l:
            res+=i
        return (res)
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = ""
        for i in s:
            if i.isalnum()==True:
                string+=i
        l = self.getReverse(string)
        print("string: ",string)
        print("l: ",l)
        if string ==l:
            return True
        return False
        # print(l)