
nums = [1,2,3]
N = len(nums)

from typing import List



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        if len(nums) == 0:
            return res
        elif len(nums) == 1:
            return res + [nums]

        for index, i in enumerate(nums):
            for sub in self.subsets(nums[index+1:]):
                res += [[i] + sub]
        return res


solution = Solution()

res = solution.subsets(nums)

print(res)

#####################################################################################################

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        L = len(nums)
        result = []

        def de_module(n,LL):

            temp = []

            while n >= 2:
                temp.append(n%2)
                n = n // 2
            temp.append(n)

            for i in range(LL-len(temp)):
                temp.append(0)
            temp.reverse()

            result = []
            for i in range(len(temp)):
                if temp[i] != 0:
                    result.append(i)
            return result




        for i in range(0, 2 ** L):
            temp = []
            itera = de_module(i, L)
    #         print(itera)
            for j in itera:
                temp.append(nums[j])
            
    #         print(temp)
            result.append(temp)
    #         print(result)

        return result



def de_module(n,LL):

    temp = []

    while n >= 2:
        temp.append(n%2)
        n = n // 2
    temp.append(n)

    for i in range(LL-len(temp)):
        temp.append(0)
    temp.reverse()

    result = []
    for i in range(len(temp)):
        if temp[i] != 0:
            result.append(i)
    return result


L = 4
for i in range(0, 2 ** L):
    de_module(14, 4)






