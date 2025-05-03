class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans=""
        maxlen=0
        count=0
        for i in s:
            if i not in ans:
                ans=ans+i
                count+=1
                maxlen=max(maxlen,count)
            else:
                count=0
                ans=ans.replace(i,"")
        return maxlen

            