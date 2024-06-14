"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

 
Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
 

Explaination:
2   0 1 0
2   0 1 0
XOR --> 0

"""

def singleNumber(nums):
    res = 0 #n ^ 0 = n

    for n in nums:
        res = n ^ res
    
    return res


nums = [4,1,2,1,2]
print(singleNumber(nums))