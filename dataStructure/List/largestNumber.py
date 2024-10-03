nums = [2,34,5,75,74,23,23,65,86,659]

largest = nums[0]

for i in range (len(nums)):
    if nums[i] > largest:
        largest = nums[i]
        i = i + 1

print(largest)