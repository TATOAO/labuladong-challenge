from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        sums = sum(nums)
        if sums % k != 0:
            return False
        buckets = [0] * k
        full_size = sums // k

        return self.backtrack(buckets, nums, full_size, 0)


    def backtrack(self, buckets: List[int], nums: List[int], full_size: int, ith_bucket:int) -> bool:
        # print(buckets, nums, k, ith_bucket)

        if sum(buckets) == full_size * len(buckets):
            return True

        if ith_bucket > len(buckets):
            return False

        for num_index in range(len(nums)):

            for bucket_index in range(len(buckets)):

                buckets[bucket_index] += nums[num_index]
                

                if buckets[bucket_index] > full_size:
                    buckets[bucket_index] -= nums[num_index]
                    continue

                elif buckets[bucket_index] == full_size:
                    ith_bucket += 1
                
                    res = self.backtrack(buckets, nums[:num_index] + nums[num_index+1:], full_size, ith_bucket)

                    ith_bucket -= 1 
                    buckets[bucket_index] -= nums[num_index]
                else:
                    res = self.backtrack(buckets, nums[:num_index] + nums[num_index+1:], full_size, ith_bucket)
                    buckets[bucket_index] -= nums[num_index]

                if res == True:
                    return True
 
        return False


solution = Solution()
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4

res = solution.canPartitionKSubsets(nums, k)
print(res)

