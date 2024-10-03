nums = [2,34,5,75,74,23,23,65,86,659]

#append    adds at last
nums.append(100)

#insert    adds at specific index
nums.insert(2, 1000)

#remove    removes specific value
nums.remove(1000)

#pop       removes at specific index
nums.pop(0)

#reverse    reverse the list
nums.reverse()

#sort       sort the list
nums.sort()

#copy      copy the list
nums2 = nums

print (nums2)

#clear     clear the list
# nums.clear()

#index     return index of value
print (nums.index(23))

#count     return count of value
print (nums.count(23))

#extend    extend the list
nums.extend(nums2)



print (nums)
