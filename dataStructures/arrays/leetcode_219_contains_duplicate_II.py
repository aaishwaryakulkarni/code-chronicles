"""
219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices
i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""

def containsDuplicates(nums, k):

    window = set()
    l = 0

    for r in range(len(nums)):
        if r - l > k:
            window.remove(nums[l])
            l += 1
        if nums[r] in window:
            return True
        window.add(nums[r])
    return False
	

nums = [1,2,3,1]
k = 3
print(containsDuplicates(nums, k))