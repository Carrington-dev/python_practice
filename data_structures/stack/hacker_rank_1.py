def perm(i, j, k, n):
    array = list([i,j,k] for i in range(i+1) for j in range(j+1) for k in range(k+1)  if i+j+k !=n)
    #array = [[i, j, k] for i in range(i) for j in range(j) for k in range(k) if (i + j + k) != n]
    return array


print(perm(1, 1, 1, 2))