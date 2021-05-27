class Solution:
    def towSum(self,nums,target):
        dict = {}
        for i, j in enumerate(nums):#i是下标index，j是里面数字item
            if target - nums[i] in dict:#从第一个开始找，如果在表中找到了，就输出结果，如果没有在哈希表中找到，就存入哈希表中、
                return i, dict[target - nums[i]]#dict[target - nums[i]]是下标
            dict[j] = i #代表着哈希表（新建的字典）输出结果是对应的下标值，也就是2=0,3=1,
nums = [2,3,6,8,9]
target = 9
a = Solution()
out = a.towSum(nums,target)
print("数组:",nums,"目标:",target,"结果:",out)
