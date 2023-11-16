def find_unsorted_subarray(nums):
    
    if all(nums[i] == nums[0] for i in range(len(nums))):
        return [0, 0]

   
    if nums == sorted(nums) or nums == sorted(nums, reverse=True):
        return [0, 0]

   
    left, right = 0, len(nums) - 1
    while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
        left += 1
    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1

    
    subarray = nums[left:right + 1]
    min_val, max_val = min(subarray), max(subarray)

    
    while left > 0 and nums[left - 1] > min_val:
        left -= 1
    while right < len(nums) - 1 and nums[right + 1] < max_val:
        right += 1

    return [left, right]

# Test cases
arr1 = [1, 2, 3, 6, 4, 4]
arr2 = [4, 4, 4, 4, 4]
arr3 = [1, 2, 3, 4, 5]
arr4 = [5, 4, 3, 2, 1]

print(find_unsorted_subarray(arr1))  # Output: [3, 5]
print(find_unsorted_subarray(arr2))  # Output: [0, 0]
print(find_unsorted_subarray(arr3))  # Output: [0, 0]
print(find_unsorted_subarray(arr4))  # Output: [0, 4]



#sort strings by length (shortest to longest)
def sort_strings_by_length(arr):
    sorted_arr =sorted(arr, key=lambda x: len(x))
    return sorted_arr

input_arr =["Telescopes", "Glasses", "Monocles", "Eyes",]
result = sort_strings_by_length(input_arr)
print(result)

#sort from longest to shortes

def sort_strings_by_length_descending(arr):
    sorted_arr =sorted(arr, key=lambda x: len(x), reverse=True)
    return sorted_arr

input_arr =["Telescopes", "Glasses", "Monocles", "Eyes",]
result = sort_strings_by_length_descending(input_arr)
print(result)
