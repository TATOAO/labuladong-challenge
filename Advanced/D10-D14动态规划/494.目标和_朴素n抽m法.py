from itertools import combinations
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.N = len(nums)
        self.sorted_nums = sorted(nums)

        possible_add_num = []
        for add_num in range(self.N+1):
            smallest = self.get_smallest(add_num)
            get_largest = self.get_largest(add_num)
            print(smallest, target, get_largest)
            if self.get_smallest(add_num) <= target <= self.get_largest(add_num):
                possible_add_num.append(add_num)
        print('finished_arrange')

        self.total_count = 0
        for add_num in possible_add_num:
            self.known_add_get_target(add_num, target)
        return self.total_count
    
    def known_add_get_target(self, add_num, target):
        for sub_list in combinations(range(self.N), add_num):
            s = 0
            for i in range(self.N):
                if i in sub_list:
                    s += self.sorted_nums[i]
                else:
                    s -= self.sorted_nums[i]
            
            if s == target:
                self.total_count += 1
                

    def get_largest(self, add_num):
        return sum(self.sorted_nums[self.N - add_num:]) - sum(self.sorted_nums[:self.N - add_num])

    def get_smallest(self, add_num):
        return sum(self.sorted_nums[:add_num]) - sum(self.sorted_nums[add_num:])

if __name__ == '__main__':
    solu = Solution()
    target = 2
    target = 35
    nums = [9,7,0,3,9,8,6,5,7,6]
    nums = [29,6,7,36,30,28,35,48,20,44,40,2,31,25,6,41,33,4,35,38]
    result = solu.findTargetSumWays(nums, target)
    print(result)
