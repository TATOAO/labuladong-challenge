from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        self.records = {}
        self.nums = nums

        def sub_rob(ith, take_last_one):
            if (ith, take_last_one) not in self.records:

                if take_last_one == 1:
                    nums = self.nums[ith+1:]
                    result = sub_rob(ith+1, 0)
                    self.records[(ith, take_last_one)] = result
                    return result
                else:
                    nums = self.nums[ith:]

                if len(nums) == 0:
                    self.records[(ith, take_last_one)] = 0
                    return 0

                if len(nums) == 1:
                    self.records[(ith, take_last_one)] = nums[0]
                    return nums[0]
                elif len(nums) == 2:
                    self.records[(ith, take_last_one)] = max(nums)
                    return max(nums)
        
                result = max(sub_rob(ith+1, 0), self.nums[ith] + sub_rob(ith+1, 1))

                self.records[(ith, take_last_one)] = result
            return self.records[(ith, take_last_one)] 

        
        result = sub_rob(0,0)
        return result

if __name__ == '__main__':
    solu = Solution()
    nums = [1,3,1,3,100]
    # nums = [2,7,9,3,1]

    result = solu.rob(nums)
    print(result)
