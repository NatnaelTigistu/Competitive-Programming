# https://leetcode.com/problems/length-of-last-word/
# Approach: Using String Property
# Time: O(n), Space: O(n)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        word = words[-1]
        return len(word)