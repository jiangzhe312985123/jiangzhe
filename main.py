class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return[i,j]
                print
        return []
# nums = [2, 7, 11, 15]
nums = [3, 2, 3, 4, 11, 7, 4]
target = 9
a = Solution()
out = a.twoSum(nums,target)
print('结果：',out)


