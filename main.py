# class Solution:
#     def twoSum(self,nums,target):
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j] == target:
#                     return[i,j]
# nums = [2, 7, 11, 15]
# nums = [3, 2, 3, 4, 11, 7, 4]
# target = 9
# a = Solution()
# out = a.twoSum(nums,target)
# print('结果：',out)
class Solution:
    def towSum(self,nums,target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]
nums = [2,3,6,7,8,9]
target = 9
a = Solution()
out = a.towSum(nums,target)
print("数组:",nums,"目标:",target,"结果:",out)


class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
nums=[1,0]
target=1
a=Solution()
out=a.twoSum(nums,target)
print(out)

