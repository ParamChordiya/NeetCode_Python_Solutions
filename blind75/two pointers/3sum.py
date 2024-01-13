import numpy as np
from typing import List
class Solution:
    # def getMat1(self,l):
    #     n = len(l)
    #     matrix = np.tile(l, (n, 1))
    #     return matrix

    # def getMat3(self,l,n):
    #     # n = len(l)
    #     matrix = np.full((n, n), l)
    #     return matrix

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # Bruteforce using matrix
        # n = len(nums)
        # mat1 = self.getMat1(nums)
        # mat2 = np.transpose(mat1)
        # matsum = mat1+mat2
        # mat3 = self.getMat3(-1,n)
        # temp_indexes=[[-1, -1, -1]]
        # for i in range(len(nums)):
        #     mat3 = self.getMat3(nums[i],n)
        #     total = mat3 + matsum
            
        #     zero_indices = np.argwhere(total == 0)
        #     m,k = np.shape(zero_indices)
        #     ref = np.full((m, 1), i)
        #     # print(ref)
        #     finalIndex = np.concatenate((ref,zero_indices),axis =1)
        #     # temp_indexes.append(finalIndex)
        #     final_matrix = np.vstack((temp_indexes, finalIndex))
        #     temp_indexes = final_matrix
        #     # print(zero_indices)
        #     # print(total)
        #     # print(finalIndex)

        # filtered_matrix = np.array([row for row in temp_indexes if len(set(row)) == len(row)])

        # new_list_of_lists = np.array([[nums[element] for element in row] for row in filtered_matrix])
        # sorted_matrix = [sorted(row) for row in new_list_of_lists]
        # unique_rows = [list(row) for row in set(tuple(row) for row in sorted_matrix)]

        # print(unique_rows)
        # return unique_rows
        # ===============================================================================
        # ===============================================================================

        res = []
        nums.sort()

        for i,a in enumerate(nums):
            # print(i,a)
            if i>0 and a == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                ressum = a + nums[l] + nums[r]
                if ressum>0:
                    r=r-1
                elif ressum<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res