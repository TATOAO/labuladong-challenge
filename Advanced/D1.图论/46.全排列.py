from typing import List

def permute(nums: List[int]) -> List[List[int]]:

    if len(nums) == 1:
        return [nums]

    res = []

    for i in range(len(nums)):

        steps_left = nums[:i] + nums[i+1:]

        res += [[nums[i]] + j for j in permute(steps_left)]

    return res




# n = [1,2,3]
# print(n[:0]+ n[1:])

# print(permute(n))




class Solution(object):
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        this function is to get all the permutation of the list by using recursion function sub
        which is to get the permutation of the list without the first element
        """
        
    
        def sub(last_time: List[List[int]], list_left: List[int]):
            if len(list_left) == 1:
                last_time.append(list_left[0])
                return [last_time], []

            else:

                result = []
                sub_list_left = []
                for i in range(len(list_left)):

                    result.append(last_time + [list_left[i]])

                    sub_list_left.append(list_left[:i] + list_left[i + 1:])

                return result, sub_list_left
        
        temp = []
        temp, sub_left = sub(temp, nums)
        
        for i in range(len(nums)-1):
            print(temp)
            sub_list = []
            sub_left_all = []
            for k in range(len(temp)):
                a,b = sub(temp[k], sub_left[k])
                sub_list += a
                sub_left_all += b
                
                
                
            temp = sub_list 
            sub_left = sub_left_all
            
        """
        temp print out 
        [[1], [2], [3], [4]]
        [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]
        [[1, 2, 3], [1, 2, 4], [1, 3, 2], [1, 3, 4], [1, 4, 2], [1, 4, 3], [2, 1, 3], [2, 1, 4], [2, 3, 1], [2, 3, 4], [2, 4, 1], [2, 4, 3], [3, 1, 2], [3, 1, 4], [3, 2, 1], [3, 2, 4], [3, 4, 1], [3, 4, 2], [4, 1, 2], [4, 1, 3], [4, 2, 1], [4, 2, 3], [4, 3, 1], [4, 3, 2]]
        """
            
        return temp
                    

solution = Solution()
solution.permute([1,2,3,4])