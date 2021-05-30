#s1=s[::-1]或者是S1=s[-1::1]
#相当于说s1是s的逆序
class Solution:
    def spread(self,s):
        if s == s[::-1]:#如果逆序是相等的，则直接返回s
            return s
        max_len = 1  #长度从1开始
        tart = s[0]  #起始位置从第一个数开始，index为0
        for i in range(len(s)-1):   #从第一个数到倒数第二数遍历
            for j in range(i+1,len(s)): #从第二个数开始到最后一个数
                if j - i + 1 >max_len and s[i:j+1] == s[i:j+1][::-1]:#如果它的长度大于已经有的最大长度，因为1的话是直接为回文了，
                    max_len = j-i+1                      #还有子序列逆序后依然相等则输出最长度为现有的长度，依次增加长度
                    tart = s[i:j+1]                       #这个是要返回的最终值，从i到j+1的值都输出。因为j+1输出的是j,
        return tart                             #不包含最后一个j+1索引对应值，但是i是包含i对应的索引对应值
s = "babad"
solution = Solution()
out = solution.spread(s)
print(out)
