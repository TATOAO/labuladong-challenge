from typing import List

class Solution:

    def removeDuplicatReserveOrder(self, nums):
        seen = set()
        seen_add = seen.add

        return [i for i in nums if not (i in seen or seen_add(i))]


    def binary_search_for_larger_point(self, nums, value):
        """
        return the index of a value than the given
        """

        if len(nums) == 0:
            return -1

        left = nums[0]
        right = nums[-1]
        mid = (right - left) // 2 + left

        while left < right:

            if value < nums[mid]:
                right = mid
                mid = (right - left) // 2 + left







    
    def lengthOfLIS(self, nums: List[int]) -> int:


        N = len(nums)

        rnums = self.removeDuplicatReserveOrder(nums)

        comap = [(value, pos) for pos,value in enumerate(rnums)]

        self.graph = []
        
        for pos, value in enumerate(rnums):
            return




        # self.graph = [
        #               [j for j, num in enumerate(nums) if num > nums[i]] 
        #               for i in range(N)]

        self.graph = [[] for _ in range(N)]
        # [[1,2,4], [2,4], ...]

        for i in range(N-1, 0, -1):
            self.graph[-i]

            



        return 0


if __name__ == '__main__':

    print('hw')
    solution = Solution()

    res = solution.lengthOfLIS([1,1,1,13,5])
    print(res)

