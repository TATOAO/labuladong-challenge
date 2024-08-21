


0 2 5
3 4 5
[-1, 0, 3, 5, 9, 12]
[0, 0, 0, 1, 0, 0]
3


0 5  -> mid 2
3 < target 5


left = 2 + 1 = 3
3 5  -> mid = 4
9 > target 5


right = mid -1  = 4 - 1 = 3
3, 3  mid = 3
left == right




---------------------------


[-1, 0, 3, 5, 9, 12]
[0, 0, 0, 1, 0, 0]
3
target 6

0 5 -> mid 2 
3 < target 6
left = 2 + 1 = 3 (value = 5)

3, 5 -> mid = 4 (value = 9)
9 > target 6
right = mid - 1 = 4 - 1 = 3 = left


##############################

[-1, 0, 3, 5, 9, 12]
target = -5

0 5 -> mid 2
3 > target -5
right = 1

0, 1 -> mid = 0
-1 > target -5
right = mid - 1= -1


break






