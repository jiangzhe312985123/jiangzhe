for i in range(1,10):
    for k in range(1,10-i):
        print(end="")
    for j in range(1,10-i):
        n = j * i
        print(str(j)+"*"+str(i)+"="+str(n)+"\t",end="")
    print()


