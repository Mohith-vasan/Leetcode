class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = ""
        maxlen = 0
        for i in s:
            if i in ans:
                index = ans.index(i)
                ans = ans[index + 1:]  
            ans += i
            maxlen = max(maxlen, len(ans))
        return maxlen
            