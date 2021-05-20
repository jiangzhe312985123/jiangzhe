#两个变量值发生变换有两种方法，一种是python自带的简单的那种
#冒泡法就是两个数字交换，两两交换
# a=10
# b=15
# c=a 10
# a=b  15
# b=c  10
# print(a)
# print(b)


# a,b =b,a
# print(a)
# print(b)

# import random
# test = []
# for i in range(100):
#     test.append(random.randint(0,1000))
# def bubble(test):
#     for k in range(0,len(test)-1):
#         for j in range(0,len(test)-1-k):
#             if test[j] > test[j+1]:
#                 a=test[j]
#                 test[j]= test[j+1]
#                 test[j+1]=a
#     return(test)
# bubble(test)
# print(test)
import random
test = []
for i in range(100):
    test.append(random.randint(0,1000))
def order(test):
    for k in range(0,len(test)-1):
        for j in range(0,len(test)-1):
            if test[j] > test[j+1]:
                test[j],test[j+1] = test[j+1],test[j]
    print(test)
order(test)#
