class Solution(object):
    def nextPermutation(self, nums):
        n=len(nums)
        ans=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ans=i
                break
        if ans==-1:
            nums.reverse()
            return nums
        for i in range(n-1,ans,-1):
            if nums[i]>nums[ans]:
                nums[i],nums[ans]=nums[ans],nums[i]
                break
        left,right=ans+1,n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums #final result
