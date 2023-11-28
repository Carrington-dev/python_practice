arr = [i for i in range(1, 20, 4)]
dic = {i:i for i in arr}
tup = tuple(list(i for i in arr))
tup_init = (1, 3, 6,)
print(len(dic))
print(dic[9])
print(tup)
print(tup_init)
