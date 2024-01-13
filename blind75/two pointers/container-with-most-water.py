from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # temp =0
        # for i, a in enumerate(height):
        #     l, r = i, len(height)-1
        #     while l<r:
        #         v = (r-l) * min(height[r],a)
        #         if v>temp:
        #             temp = v
        #         r-=1
        # return temp

        res = 0
        l,r = 0, len(height)-1
        while l<r:
            area = (r-l)*min(height[l],height[r])
            res = max(res,area)
            if height[l]>height[r]:
                r-=1
            elif height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res
                

        # d = {}
        # res = 0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         # print(i,j)
        #         temp = (j-i)*min(height[j],height[i])
        #         if temp>res:
        #             res =temp
        #         if temp in d:
        #             d[temp]+= [(i,j)]
        #         else:
        #             d[temp] = [(i,j)]
        # d = dict(sorted(d.items()))
        # k = list(d.keys())
        # print(k)
        # maxEle = k[-1]
        
        # print(d[maxEle])

        # return res

        # volume = 0 
        # for i, a in enumerate(height):
        #     # print(i,a)
            
        #     l, r = i , len(height)-1
            
        #     while l<r:
        #         print(l,r)
        #         print(height[l], height[r])
                
        #         print("===========")
        #         temp = ((r-l)*min(height[l],height[r]))
        #         print(temp)
        #         if temp>volume:
        #             volume = temp
        #         r=r-1
        # return volume
        