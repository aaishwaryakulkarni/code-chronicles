"""
Maximum Sum Increasing Subsequence | DP-14

Given an array of n positive integers. Write a program to find the sum of maximum
sum subsequence of the given array such that the integers in the subsequence are 
sorted in increasing order.

For example, if input is {1, 101, 2, 3, 100, 4, 5},
then output should be 106 (1 + 2 + 3 + 100),

if the input array is {3, 4, 5, 10},
then output should be 22 (3 + 4 + 5 + 10) and 

if the input array is {10, 5, 4, 3},
then output should be 10

"""

def maxSum(nums):
	dp = [i for i in nums]

	for i in range(1, len(nums)):
		for j in range(i):

			if(nums[i] > nums[j]):

				dp[i] = max(nums[i] + dp[j], dp[i])

	return max(dp)

nums = [1, 101, 2, 3, 100, 4, 5]
print(maxSum(nums))



