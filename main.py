 #九九乘法表
for i in range(9,0,-1):
    for j in range(i,0,-1):
        print(str(i) + str("*") + str(j) + "=" + str(i*j),end="\t")
    print()