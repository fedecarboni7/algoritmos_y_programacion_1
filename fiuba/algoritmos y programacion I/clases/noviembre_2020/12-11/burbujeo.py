def burbujeo(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j] #linea a tener en cuenta
    return l

l = [4,2,3,5,1,3]

print(burbujeo(l))