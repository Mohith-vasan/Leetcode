class Solution(object):
    def twoSum(self, nums, target):
        if len(nums)==0 or len(nums)==1:
            return
        arr=[]
        for i in range(len(nums)):
            arr.append([nums[i],i])
        arr.sort()
        Left,Right=0,len(arr)-1
        while Left<Right:
            mid=arr[Left][0]+arr[Right][0]
            if mid==target:
                return [arr[Left][1],arr[Right][1]]
            elif mid<target:
                Left+=1
            else:
                Right-=1
    
