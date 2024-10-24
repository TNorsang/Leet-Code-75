def move_zeros(nums):   
    left = right = 0
    while right != len(nums):
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
        right += 1
    return nums