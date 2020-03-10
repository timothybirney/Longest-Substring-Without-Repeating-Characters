# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 08:08:22 2020

@author: Owner

Given a string, find the length of the longest substring without repeating
 characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence
             and not a substring.

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # substring, length of substring, pointers and length of string
        sub = ''
        lsub = len(sub)
        i = j = 0
        end = len(s)

        # check for no duplicate characters using len and set
        if len(set(s)) == len(s):
            lsub = len(s)

        # sliding window
        else:
            while i < end:
                while j < end:

                    # get string, length of string, and length of unique
                    # characters using len and set
                    string = s[i:j+1]
                    lstring = len(string)
                    lset = len(set(string))

                    # check for duplicates,
                    # if yes: move right pointer past end
                    if lset < lstring:
                        j = end + 1

                    # check for duplicates,
                    # if no: compare and update substring, move right pointer
                    else:
                        if lstring > lsub:
                            lsub = lstring
                        j += 1

                # move left pointer
                # move right pointer to left pointer
                i += 1
                j = i

        return(lsub)


print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring('bbbbb'))
print(Solution().lengthOfLongestSubstring('pwwkew'))
print(Solution().lengthOfLongestSubstring(' '))
print(Solution().lengthOfLongestSubstring(''))
print(Solution().lengthOfLongestSubstring('au'))
