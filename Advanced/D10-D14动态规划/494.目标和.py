
from itertools import combinations
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if nums == []:
            return 0
        self.nums = nums
        self.N = len(self.nums)

        self.records = {} 
        return self.sub(0, target)


    def sub(self, nth, target):

        if (nth, target) in self.records:
            return self.records[(nth,target)]

        if self.N == nth:
            if target == 0:
                self.records[(nth,target)] = 1
            else:
                self.records[(nth,target)] = 0
        else:
            val = self.nums[nth]
            self.records[(nth,target)] = self.sub(nth+1, target-val) + self.sub(nth+1, target+val) 

        return self.records[(nth,target)]


if __name__ == '__main__':
    solu = Solution()
    target = 2
    target = 35
    nums = [9,7,0,3,9,8,6,5,7,6]
    nums = [29,6,7,36,30,28,35,48,20,44,40,2,31,25,6,41,33,4,35,38]
    result = solu.findTargetSumWays(nums, target)
    print(result)
