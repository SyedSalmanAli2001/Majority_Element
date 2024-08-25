# Majority Element
nums = [4,5,4,5,4,5,5,4,4]


def majority_element(nums):
    flag_a = 0
    flag_b = 0
    element = 0
    for i in range(len(nums)):
        if nums[i] == nums[0]:
            flag_a += 1
        if nums[i] != nums[0]:
            flag_b += 1
            element = nums[i]
    if flag_a > len(nums)/2:
        return nums[0]
    else:
        return element


print(majority_element(nums))