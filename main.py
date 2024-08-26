# Majority Element - Boyer-Moore Voting Algorithm
nums_array = [5, 1, 4, 5, 2, 4, 5, 5, 5]


def majority_element(array):
    result, count = 0, 0
    for i in range(len(array)):
        if count == 0:
            result = array[i]
        if array[i] == result:
            count += 1
        elif array[i] != result:
            count -= 1
    return result


print(majority_element(nums_array))
