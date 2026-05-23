def giaithua(a):
    gt=1
    for i in range(1, a + 1):
        gt=gt*i
    return gt
n = int(input("nhap vao mot so nguyen duong: "))
print("%d!=%d"%(n,giaithua(n)))
