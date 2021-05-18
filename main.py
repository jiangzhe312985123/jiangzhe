for i in range(1,10):
    for k in range(1,10-i):
        print(end="        ")
    for j in range(1,i+1):
        n = i * j
        print(str(j)+"*"+str(i)+"="+str(n)+"\t",end="")
    print()


