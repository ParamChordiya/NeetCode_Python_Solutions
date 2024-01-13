from typing import List
# class Solution:
#     def anagramProfile(self,a):
#         return list(a)

#     def checkAnagram(self,a,b):
#         la = self.anagramProfile(a)
#         la.sort()
#         lb = self.anagramProfile(b)
#         lb.sort()
#         if  la == lb:
#             return True
#         return False

#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         l = len(strs)
#         result = []
        
#         while strs:
#             a = strs[0]
#             temp=[a]
#             strs.remove(a)
#             i = 0
#             while i<len(strs):
#                 b = strs[i]
#                 if self.checkAnagram(a,b):
#                     temp.append(b)
#                     strs.remove(b)
#                 else:
#                     i+=1
#             result.append(temp)
#         print(result)
#         return result

class Solution:
    def anagramProfile(self, a):
        return ''.join(sorted(a))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            profile = self.anagramProfile(s)
            print('profile: ',profile)
            if profile in anagrams:
                anagrams[profile].append(s)
            else:
                anagrams[profile] = [s]

        print(anagrams)
        return list(anagrams.values())