class Solution:
    def isValid(self, s: str) -> bool:
        #create a hashmap
        braceMap = {
            ']':'[',
            ')':'(',
            '}':'{'
            }
        #create a stack array
        stack = []

        for i in s: # for each charachter in string
            if i in braceMap: #if the charachter is a closing brace then
                if stack and stack[-1] == braceMap[i]: #if stack is not empty and last char of stack is same as opening of the current closer
                    stack.pop() #remove that from stack
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
        