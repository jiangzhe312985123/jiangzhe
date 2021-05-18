for i in range(1, 10):
    for j in range(1, i+1):
        n = j * i
        # 1*1  1*1,2   1*1,2,3
        # print('{}*{}={}'.format(i,j,i*j), end='\t')
        # print("%d * %d = %d" %i,j,i*j)
        # print("i*j",end=/t)
        # print(str(i)+"*"+str(j)+'='+str(n)+'\t', end="")
        print(str(j), '*', str(i), '=', str(n), '\t', end="")
    print()


for i in range(1,10):
    for j in range(1,i+1):
        n = i * j
        print(str(i)+"*"+str(j)+"="+str(n)+"\t",end='')
    print()


