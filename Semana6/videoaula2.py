def nfat(L):
    n=0
    fat=1
    while fat<=L:
        n+=1
        fat*=n
    print(n-1)
    return (n-1)


nfat(1000000)
