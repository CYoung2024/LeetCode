class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            temp = s[i]
            for j in range(i+1,len(s)):
                if temp.find(s[j]) == -1:
                    temp += s[j]
                else:
                    if len(temp) > longest:
                        longest = len(temp)
                    temp = ""
            if len(temp) > longest:
                longest = len(temp)
            if longest > 32:
                break
        return longest