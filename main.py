def solution(nums,target):
	#如果列表长度小于2，则直接结束
    if len(nums) < 2:
        return
        #两次循环列表，分别对列表中的所有可能的数字进行相加
        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

