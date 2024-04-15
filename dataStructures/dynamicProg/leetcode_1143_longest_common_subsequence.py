"""
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common 
subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string 
with some characters (can be none) deleted without changing the relative order 
f the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to 
both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

"""

def longestCommonSubsequence(text1, text2):

    t1 = len(text1)
    t2 = len(text2)

    matrix = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):

            if text1[i] == text2[j]:
                matrix[i][j] = 1 + matrix[i + 1][j + 1]
            else:
                matrix[i][j] = max(matrix[i][j + 1],matrix[i + 1][j])
    
    print(matrix)
    return matrix[0][0]


text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1, text2))