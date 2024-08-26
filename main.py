# Majority Element - Hashmap Solution
num = [5, 1, 4, 5, 2, 2, 2, 2, 2, 2]


def majority_element(nums_array):
    count = {}
    res, max_count = 0, 0
    for n in nums_array:
        count[n] = 1 + count.get(n, 0)
        res = n if count[n] > max_count else res
        max_count = max(count[n], max_count)
    return res


print(majority_element(num))

# def majority_element(array):
#     result, count = 0, 0
#     for i in range(len(array)):
#         if count == 0:
#             result = array[i]
#         if array[i] == result:
#             count += 1
#         elif array[i] != result:
#             count -= 1
#     return result
#
#
# print(majority_element(nums_array))
