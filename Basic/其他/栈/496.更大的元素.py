from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        self.records = {}

        self.stack = []

        for i in nums2:

            j = 0
            N = len(self.stack)
            if N == 0:
                self.stack.append(i)

            while j < N :
                last_element = self.stack[-1]
                if last_element < i:
                    self.records[last_element] = i
                    self.stack.pop()
                else:
                    self.stack.append(i)
                    break
                j += 1

        result = []
        for i in nums1:
            if i in self.records:
                result.append(i)
            else:
                result.append(i)

        return result

            

if __name__ == '__main__':
    solu = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    nums2 = [5,4,2,3,9]
    result = solu.nextGreaterElement(nums1, nums2)
    print(result)






