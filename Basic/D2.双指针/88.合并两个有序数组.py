from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        temp = []
        i = 0
        j = 0
        index = 0
        while i < m or j < n:

            if i == m and j < n:
                temp.append(nums2[j])
                j += 1
                continue
            elif i < m and j == n:
                temp.append(nums1[i])
                i += 1
                continue

            # nums1 比较小
            if nums1[i] <= nums2[j] :
                temp.append(nums1[i])
                i += 1
            # nums2 比较小
            else:
                temp.append(nums2[j])
                j += 1
            index += 1

        nums1 = temp



if __name__ == '__main__':
    solu = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solu.merge(nums1, m, nums2, n)




class Father:
    function_lists: List = []

    def regitser(self):
        pass

class Son(Father):

    @register
    def funcitonA(self):
        pass


    @register
    def funcitonB(self):
        pass


