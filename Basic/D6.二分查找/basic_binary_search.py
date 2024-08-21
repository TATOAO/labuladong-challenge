nums = [-1,0,3,5,9,12]


def binary_search_right_bound(target):
    N = len(nums)
    left, right = 0, N - 1
    while left < right:
        mid = left + (right - left)//2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid + 1

    if left ==  N - 1:
        return -1

    if left == target :
        return left + 1
    elif left > target:
        return 0
    else:
        return -1

    return mid

t = 100
result = binary_search_right_bound(t)
nums = [-1,0,3,5,9,12]
print(nums)
print([0 for i in range(result)] + [1] + [0 for i in range(len(nums) - result - 1)])
print(result)
print('target', t)
