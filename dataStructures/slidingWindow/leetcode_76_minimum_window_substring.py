"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

"""

def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    if t == "":
        return ""
    
    window, countT = {}, {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)
    
    have, need = 0 , len(countT)
    res, resLen = [-1, -1], float("infinity")
    l = 0

    for r in range(len(s)):
        c = s[r]

        window[c] = 1 + window.get(c,  0)

        if c in countT and window[c] == countT[c]:
            have = have + 1
        
        while have == need:

            if(r - l + 1) < resLen:
                res = [l, r]
                resLen = r - l + 1
            
            #pop from left
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have = have - 1
            
            l = l + 1

    l, r  = res
    return s[l: r + 1] if resLen != float("infinity") else ""        


s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s,t))