from typing import Dict, List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        # delete repeated numbers
        temp = nums[0]
        new_list = [temp]
        for i in nums[1:]:
            if i != temp:
                new_list.append(i)

        N = len(new_list)

        possible_next_nums: Dict[int, List[int]] = {}

        for i in range(0,N):
            current_num = new_list[i]
            possible_next = []
            for j in range(i,N):
                if new_list[j] > current_num:
                    possible_next.append(j)
            possible_next_nums[i] = possible_next

        records = {}
        def LIS(pos:int) -> int:
            if pos in records:
                return records[pos]

            pathes = possible_next_nums[pos]
            if len(pathes) == 0:
                records[pos] = 1
                return 1
            
            result = max(LIS(next_pos) for next_pos in pathes) + 1
            records[pos] = result
            return result

        return max(LIS(i) for i in range(N-1, -1, -1))


if __name__ == '__main__':
    solu = Solution()
    nums = [10,9,2,5,3,7,101,18]

    result = solu.lengthOfLIS(nums)
    print(result)

